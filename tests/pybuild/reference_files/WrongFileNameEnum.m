classdef SimulinkEnumTwo < Simulink.IntEnumType

    enumeration
        Zero(0)
        One(1)
        Two(2)
        Three(3)
    end

    methods (Static)
        function retVal = SimulinkEnumTwo()
            retVal = 'SimulinkEnum';
        end
        function retVal = getDefaultValue()
            retVal = SimulinkEnumTwo.Three;
        end
        function retVal = getDataScope()
            retVal = 'Exported';
        end
        function retVal = addClassNameToEnumNames()
            retVal = true;
        end
    end
end
