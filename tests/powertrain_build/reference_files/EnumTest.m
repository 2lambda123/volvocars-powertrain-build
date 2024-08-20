classdef EnumTest < Simulink.IntEnumType

    enumeration
        ClimaOff(0)
        ClimaHeatgToHvacAndHvBatt(1)
        ClimaHeatgToHvBatt(2)
        ClimaHeatgToHvac(3)
        ClimaFlow(4)
        Degas(5)
        FailSafe(6)
    end

    methods (Static)
        function retVal = getDescription()
            retVal = 'EnumTest';
        end
        function retVal = getDefaultValue()
            retVal = EnumTest.ClimaOff;
        end
        function retVal = getDataScope()
            retVal = 'Exported';
        end
        function retVal = addClassNameToEnumNames()
            retVal = true;
        end
    end
end
