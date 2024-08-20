# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Constant defining the expected result from reading the core config file,
using ReadCoreIds.get_core_ids_proj, and for usage by the feature config class
"""

CORE_CFG = {
    'CFG1': {
        'EventIDs': {
            'VcEvAmbPCompPlausMon': 'Event Id for Ambient Pressure rationality monitor '
                                    '(comparison to other sensor at eng off)',
            'VcEvCacPCompPlausMon': 'Event Id for CAC Pressure Rationality Monitor '
                                    '(comparison to other sensor at eng off)'
        },
        'FunctionIDs': {
            'VcFiAmbPCompPlausMon': 'VcFi forAmbient Pressure Rationality Monitor  '
                                    '(comparison to other sensor at eng off)',
            'VcFiCacPCompPlausMon': 'VcFi for CAC Pressure Rationality Monitor  '
                                    '(comparison to other sensor at eng off)'
            },
        'IUMPR': {
            'Vc09BoostHiPlausMon': 'Ratio Id for Boost Pressure High Rationality Monitor',
            'Vc09BoostLoPlausMon': 'Ratio Id for Boost Pressure Low '
                                   'Rationality Monitor'
        },
        'Mode$06': {
            'Vc06BoostHiPlausMon': ('Test Result Id for high boost pressure Monitoring',
                                    '17'),
            'Vc06BoostLoPlausMon': ('Test Result Id for low boost pressure Monitoring',
                                    '18')
        },
        'Ranking': {
            'VcRvAmbPCompPlausMon': 'Ranking Id for Ambient Pressure Rationality Monitor',
            'VcRvCacPAmbPPlausMon': 'Ranking Id for CAC pressure vs Ambient pressure test'
        }
    },
    'CFG2': {
        'EventIDs': {
            'VcEvAmbPCompPlausMon':
                'Event Id for Ambient Pressure rationality monitor (comparison to other sensor at eng off)',
            'VcEvExhMnfldPCompPlausMon':
                'Event Id for Exhaust Manifold Rationality Monitor (comparison to other sensor at eng off)'
        },
        'FunctionIDs': {
            'VcFiAmbPCompPlausMon':
                'VcFi forAmbient Pressure Rationality Monitor  (comparison to other sensor at eng off)',
            'VcFiExhMnfldPCompPlausMon':
                'VcFi for Exhaust Manifold Pressure Diff Rationality Monitor (comparison to other sensor at eng off)'
            },
        'IUMPR': {
            'Vc09BoostHiPlausMon': 'Ratio Id for Boost Pressure High Rationality Monitor',
            'Vc09Boost1HiPlausMon': 'Ratio Id for Boost Pressure 1 High Rationality Monitor'
        },
        'Mode$06': {
            'Vc06BoostHiPlausMon': ('Test Result Id for high boost pressure Monitoring',
                                    '17'),
            'Vc06Boost1HiPlausMon': ('Test Result Id for high boost pressure 1 Monitoring',
                                     '1A')
        },
        'Ranking': {
            'VcRvAmbPCompPlausMon': 'Ranking Id for Ambient Pressure Rationality Monitor',
            'VcRvCacPIntkPPlausMon': 'Ranking Id for Exhaust Manifold Pressure '
                                     'Rationality Monitor (sensor vs model)'
        }
    }
}
