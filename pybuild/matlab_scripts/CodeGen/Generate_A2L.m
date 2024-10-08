% Copyright 2024 Volvo Car Corporation
% Licensed under Apache 2.0.

function Generate_A2L(CodegenFunction, A2lStylesheetName, model_ending)
    if nargin < 3
        model_ending = '_Tmp';
    end
    fprintf('\n\nGeneration of %s started\n\n', [CodegenFunction '.a2l']);
    workspace = getenv('WORKSPACE');
    tl_config_dir = fullfile([workspace, '/ConfigDocuments/TL4_3_settings']);
    if exist(tl_config_dir, 'dir')
        TargetInfoDir = fullfile([tl_config_dir '/TargetInfo']);
        TargetConfigDir = fullfile([tl_config_dir '/TargetConfig']);
    else
        TargetInfoDir = fullfile([getenv('TL_ROOT') '/Matlab/TL/ApplicationBuilder/BoardPackages/HostPC64/MSVC']);
        TargetConfigDir = fullfile([getenv('TL_ROOT') '/Matlab/TL/TargetConfiguration/x86_64/MSVC']);
    end

    ApplicationName = [CodegenFunction model_ending];
    BuildName = ['Build' CodegenFunction model_ending];

    dsdd_manage_build('Create',...
       'Name', BuildName,...
       'Application', ApplicationName,...
       'TargetInfoDir', TargetInfoDir,...
       'TargetConfigDir', TargetConfigDir);

    enumDataTypesObj = dsdd('CreateEnumDataTypes', ['/' ApplicationName '/' BuildName]);
    enumNames = GetUsedEnumerations(CodegenFunction);
    for idx = 1:length(enumNames)
        enumName = enumNames{idx};
        underlyingDataType = CalculateUnderlyingDataType(CodegenFunction, enumName);
        [hDDTypedef, ~, ~] = tlEnumDataType('CreateDDTypedef',...
            'SLEnumType', enumName,...
            'TypedefGroup', ['/' ApplicationName '/' BuildName '/EnumDataTypes'],...
            'CreateTemplate', 'off');
        dsdd('SetUnderlyingEnumDataType', hDDTypedef, underlyingDataType);
        dsdd('SetTag', hDDTypedef, [enumName '_tag']);
    end

    dsdd_export_a2l_file(...
        'Application', ApplicationName,...
        'Build', BuildName,...
        'TargetInfoDir', TargetInfoDir,...
        'TargetConfigDir', TargetConfigDir,...
        'StyleSheet',   A2lStylesheetName,...
        'File', [CodegenFunction '.a2l'],...
        'ProjectFrame', 'off',...
        'OverwriteCalProperties', 'on',...
        'MergeA2lModules', 'on',...
        'asap2version', '1.40',...
        'UseLookupStructures', 'off',...
        'ExternalVariables', 'on',...
        'UseUnderlyingEnumDataTypeInfo', 'on');

    % Delete created enums, these can cause problems for upcoming code generation calls on models
    % using the same enumerations.
    dsdd('Delete', enumDataTypesObj);

    fprintf('\n\nGeneration of %s finished\n\n', [CodegenFunction '.a2l']);
end

function enumerations = GetUsedEnumerations(modelName)
%GETUSEDENUMERATIONS Get all enumeration names used in a given model.
    unsupportedByTLAPI = {'TL_DummyTrigger', 'TL_Enable', 'TL_Function', 'TL_SimFrame'};
    tlBlocksTmp = find_system(modelName, 'FindAll', 'on', 'LookUnderMasks', 'All', 'RegExp', 'on', 'MaskType', 'TL_*');
    maskTypesTmp = get_param(tlBlocksTmp, 'MaskType');
    supportedTlBlocks = tlBlocksTmp(ismember(maskTypesTmp, unsupportedByTLAPI)==0);
    [allDataTypes, invalidIndices, ~] = tl_get(supportedTlBlocks, 'output.type');
    validTlBlocks = supportedTlBlocks(~invalidIndices);
    validDataTypes = allDataTypes(~invalidIndices);
    enumBlocks = validTlBlocks(strcmp(validDataTypes, 'IMPLICIT_ENUM'));
    unitsTmp = tl_get(enumBlocks, 'output.unit');
    if ~iscell(unitsTmp)
        unitsTmp = {unitsTmp};
    end
    if ~isempty(unitsTmp)
        units = unitsTmp(cellfun(@(x) ~isempty(x), unitsTmp));
        enumerations = unique(erase(units, ['-', ',', '$']));
    else
        enumerations = {};
    end
end

function underlyingDataType = CalculateUnderlyingDataType(modelName, enumName)
%CALCULATEUNDERLYINGDATATYPE Calculate best fitting data type given a name of an enumeration.
%   This is done by find min and max values, than choosing a fitting data type, as small as possible.
    enumMemberNames = enumeration(enumName);
    if isempty(enumMemberNames)
        error([...
            'Cannot get enum name %s from model %s.',...
            'Enum name should match the unit in applicable blocks, e.g. -,$EnumName.'...
            ], enumName, modelName);
    end
    % int32 is super class of Simulink.IntEnumType
    enumMemberValues = int32(enumMemberNames);
    minValue = min(enumMemberValues);
    maxValue = max(enumMemberValues);

    % TODO Consider forcing signed like CS (or ARXML, from database?) does, seems to be int8 specifically
    underlyingDataType = '';
    if minValue >= 0
        if maxValue <= 255
            underlyingDataType = 'UInt8';
        elseif maxValue <= 65535
            underlyingDataType = 'UInt16';
        end
    elseif minValue >= -128
        if maxValue <= 127
            underlyingDataType = 'Int8';
        elseif maxValue <= 32767
            underlyingDataType = 'Int16';
        end
    elseif minValue >= -32768
        if maxValue <= 32767
            underlyingDataType = 'Int16';
        end
    end

    if isempty(underlyingDataType)
        error(...
            'Unhandled enum size, name: %s, min: %s, max: %s. Valid types are uint8/16 and int8/16',...
            enumName, minValue, maxValue);
    end
end
