% Copyright 2024 Volvo Car Corporation
% Licensed under Apache 2.0.

function updateCodeSwConfig(RootFolder, model_path)
    % updateCodeSwConfig(RootFolder, model_path)
    %
    % Executes 'py -3.6 -m powertrain_build.config models' for the model.
    % This script reads the .json, .c and .h-files and looks for configs for
    % the variables that already have a config in the json.
    %
    % Arguments:
    % RootFolder: Pull path to pt_pcc
    % model_path: Path to the model to regenerate config for.
    old_pythonpath = getenv('PYTHONPATH');

    [~, out]=system(['CALL %PYTOOLS_ACTIVATE% & python -m powertrain_build.config models "' model_path '"']);

    disp(out)
    setenv('PYTHONPATH', old_pythonpath)
end
