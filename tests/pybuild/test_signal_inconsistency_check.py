"""Test signal_inconsistency_check.py"""

import os
import unittest
from argparse import Namespace
from unittest.mock import MagicMock, patch

from powertrain_build.signal_inconsistency_check import (
    EXIT_CODE_INCORRECT_CSV,
    EXIT_CODE_MISSING_CONSUMER,
    EXIT_CODE_NEVER_ACTIVE_SIGNALS,
    EXIT_CODE_OK,
    EXIT_CODE_UNPRODUCED,
    SignalInconsistency,
)

MODEL_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestSignalInconsistency(unittest.TestCase):
    """Test SignalInconsistency"""

    @classmethod
    def setUpClass(cls):
        """Common objects and variables"""
        cls._args = Namespace(models=["test_model", "test_model1"], ci_url="")
        cls._args1 = Namespace(
            models=["test_model", "test_model1", "test_model2"], ci_url=""
        )
        cls._skip_all_ext = {"mdl1": {"sig1_ext"}, "mdl2": {"sig2_ext", "sig3_Ext"}}
        cls._used_inports = {"sig_1", "sig_2", "sig_22", "sig_3"}
        cls._sig_incons = SignalInconsistency(TestSignalInconsistency._args1)

    def test_get_model_names_from_gerrit(self):
        """Test _get_mode_names_from_gerrit"""
        paths = [
            os.path.join("Models", "SSPPL", "VcDepExt", "VcDepExt.mdl"),
            os.path.join("Models", "SSPTHM", "VcAmbMod", "VcAmbMod.mdl"),
            os.path.join("Models", "SSPTHMC", "VcAcCtrl", "VcAcCtrl.mdl"),
        ]
        result = SignalInconsistency(TestSignalInconsistency._args)._get_model_names(
            paths
        )
        expected_result = ["VcDepExt", "VcAmbMod", "VcAcCtrl"]
        self.assertEqual(result, expected_result)

    def test_check_unproduced_signals(self):
        """Test check_unproduced_signals"""
        unproduced_signals = {
            "test_model": {
                "sVcAcCtrl_D_ElacDiagcFb": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "sVcAc_D_AirCondCmpsrStats": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "sVcAc_D_CoolgForHvBattSts": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "signal_B_dummytestingSts": [{"GEP3_BEV"}],
            },
            "test_model1": {
                "sVcAcCtrl_D_Elac": [{"VEP"}],
                "sVcAc_D_Air": [{"VEP"}],
                "sVcAc_D_Cool": [{"VEP"}],
            },
        }
        exit_code, _ = SignalInconsistency(
            TestSignalInconsistency._args
        ).check_unproduced_signals(unproduced_signals)
        self.assertEqual(exit_code, EXIT_CODE_UNPRODUCED)

    def test_check_never_active_signals(self):
        """Test check_never_active_signals"""
        exit_code, _ = SignalInconsistency(
            TestSignalInconsistency._args
        ).check_never_active_signals({})
        self.assertEqual(exit_code, EXIT_CODE_OK)

        never_active_signals = {
            "test_model": {
                "sVcNeverActiveOne_B_SomethingFalse": [{"GEP3_BEV"}, {"VED"}, {"SPA"}]
            },
            "test_model1": {"sVcNeverActiveTwo_B_SomethingFalse": [{"VEP"}]},
        }
        exit_code, _ = SignalInconsistency(
            TestSignalInconsistency._args
        ).check_never_active_signals(never_active_signals)
        self.assertEqual(exit_code, EXIT_CODE_NEVER_ACTIVE_SIGNALS)

    def test_check_missing_consumer_signals(self):
        """Test check_missing_consumer_signals"""
        missing_consumer_signals = {
            "test_model": {
                "sVcAcCtrl_D_ElacDiagcFb": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "sVcAc_D_AirCondCmpsrStats": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "sVcAc_D_CoolgForHvBattSts": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
            },
            "test_model1": {
                "ElacDiagcFb": [{"VEP"}],
                "AirCondCmpsrStats": [{"VEP"}],
                "CoolgForHvBattSts": [{"VEP"}],
            },
        }

        skip_all = {
            "test_model": {
                "sVcAcCtrl_D_ElacDiagcFb",
                "sVcAc_D_AirCondCmpsrStats",
                "sVcAc_D_CoolgForHvBattSts",
            },
            "test_model1": {"ElacDiagcFb", "AirCondCmpsrStats", "CoolgForHvBattSts"},
        }
        keep_all = {"test_model": {}, "test_model1": {}}

        signal_inconsistency = SignalInconsistency(TestSignalInconsistency._args)

        # Check that method return correct exit code if signals are missing consumers.
        signal_inconsistency.fetch_signals_to_skip = MagicMock(return_value=keep_all)
        exit_code, _ = signal_inconsistency.check_missing_consumer_signals(
            missing_consumer_signals
        )
        self.assertEqual(exit_code, EXIT_CODE_MISSING_CONSUMER)

        # Check that method return correct exit code if signals are added to <mdl>Unconsumed.csv.
        signal_inconsistency.fetch_signals_to_skip = MagicMock(return_value=skip_all)
        exit_code, _ = signal_inconsistency.check_missing_consumer_signals(
            missing_consumer_signals
        )
        self.assertEqual(exit_code, EXIT_CODE_OK)

    def test_sort_internal_inconsistency_by_model(self):
        """Test _sort_internal_inconsistency_by_model"""

        signal_inconsistency_results = {
            "GEP3_BEV": {
                "sigs": {
                    "int": {
                        "test_model": {
                            "missing": {
                                "sVcAcCtrl_D_ElacDiagcFb": {"GEP3_BEV"},
                                "sVcAc_D_AirCondCmpsrStats": {"GEP3_BEV"},
                                "sVcAc_D_CoolgForHvBattSts": {"GEP3_BEV"},
                                "signal_B_dummytestingSts": {"GEP3_BEV"},
                            },
                            "unused": {
                                "sVcAcCtrl_D_ElacDiagcFb": {"GEP3_BEV"},
                                "sVcAc_D_AirCondCmpsrStats": {"GEP3_BEV"},
                                "sVcAc_D_CoolgForHvBattSts": {"GEP3_BEV"},
                            },
                        }
                    }
                },
                "never_active_signals": {},
            },
            "VED": {
                "sigs": {
                    "int": {
                        "test_model": {
                            "missing": {
                                "sVcAcCtrl_D_ElacDiagcFb": {"VED"},
                                "sVcAc_D_AirCondCmpsrStats": {"VED"},
                                "sVcAc_D_CoolgForHvBattSts": {"VED"},
                            },
                            "unused": {
                                "sVcAcCtrl_D_ElacDiagcFb": {"VED"},
                                "sVcAc_D_AirCondCmpsrStats": {"VED"},
                                "sVcAc_D_CoolgForHvBattSts": {"VED"},
                            },
                        }
                    }
                },
                "never_active_signals": {},
            },
            "VEP": {
                "sigs": {
                    "int": {
                        "test_model1": {
                            "missing": {
                                "sVcAcCtrl_D_Elac": {"VEP"},
                                "sVcAc_D_Air": {"VEP"},
                                "sVcAc_D_Cool": {"VEP"},
                            },
                            "unused": {
                                "ElacDiagcFb": {"VEP"},
                                "AirCondCmpsrStats": {"VEP"},
                                "CoolgForHvBattSts": {"VEP"},
                            },
                        }
                    }
                },
                "never_active_signals": {},
            },
            "SPA": {
                "sigs": {
                    "int": {
                        "test_model": {
                            "missing": {
                                "sVcAcCtrl_D_ElacDiagcFb": {"SPA"},
                                "sVcAc_D_AirCondCmpsrStats": {"SPA"},
                                "sVcAc_D_CoolgForHvBattSts": {"SPA"},
                            },
                            "unused": {
                                "sVcAcCtrl_D_ElacDiagcFb": {"SPA"},
                                "sVcAc_D_AirCondCmpsrStats": {"SPA"},
                                "sVcAc_D_CoolgForHvBattSts": {"SPA"},
                            },
                        },
                        "test_model2": {
                            "missing": {
                                "sVcAcCtrl_D_Elac": {"SPA"},
                                "sVcAc_D_Air": {"SPA"},
                                "sVcAc_D_Cool": {"SPA"},
                            }
                        },
                    }
                },
                "never_active_signals": {
                    "test_model": [
                        "sVcNeverActiveOne_B_SomethingFalse",
                        "sVcNeverActiveTwo_B_SomethingFalse",
                    ]
                },
            },
        }
        expected_output_missing = {
            "test_model": {
                "sVcAcCtrl_D_ElacDiagcFb": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "sVcAc_D_AirCondCmpsrStats": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "sVcAc_D_CoolgForHvBattSts": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "signal_B_dummytestingSts": [{"GEP3_BEV"}],
            },
            "test_model1": {
                "sVcAcCtrl_D_Elac": [{"VEP"}],
                "sVcAc_D_Air": [{"VEP"}],
                "sVcAc_D_Cool": [{"VEP"}],
            },
            "test_model2": {
                "sVcAcCtrl_D_Elac": [{"SPA"}],
                "sVcAc_D_Air": [{"SPA"}],
                "sVcAc_D_Cool": [{"SPA"}],
            },
        }
        expected_output_unused = {
            "test_model": {
                "sVcAcCtrl_D_ElacDiagcFb": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "sVcAc_D_AirCondCmpsrStats": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
                "sVcAc_D_CoolgForHvBattSts": [{"GEP3_BEV"}, {"VED"}, {"SPA"}],
            },
            "test_model1": {
                "ElacDiagcFb": [{"VEP"}],
                "AirCondCmpsrStats": [{"VEP"}],
                "CoolgForHvBattSts": [{"VEP"}],
            },
        }
        expected_output_never_active = {
            "test_model": {
                "sVcNeverActiveOne_B_SomethingFalse": [{"SPA"}],
                "sVcNeverActiveTwo_B_SomethingFalse": [{"SPA"}],
            }
        }

        signal_inconsistency = SignalInconsistency(TestSignalInconsistency._args1)
        signal_inconsistency.signal_inconsistency_results = signal_inconsistency_results
        (
            output_missing,
            output_unused,
            output_never_active,
        ) = signal_inconsistency._sort_internal_inconsistency_by_model()

        self.assertDictEqual(output_missing, expected_output_missing)
        self.assertEqual(output_unused, expected_output_unused)
        self.assertDictEqual(output_never_active, expected_output_never_active)

    def test_merge_tuple_list(self):
        """Test _merge_tuple_list"""
        test_data = {
            "test_model": [
                ("signal1", {"GEP3_HEP7"}),
                ("signal1", {"VED4_GEN3"}),
                ("signal2", {"GEP3_HEP7"}),
            ],
            "test_model2": [
                ("sig1", {"GEP3_HEP7"}),
                ("sig2", {"VED4_GEN3"}),
                ("sig1", {"SPA"}),
            ],
            "test_model3": [("si1", {"GEP3"}), ("si1", {"VED4"}), ("si1", {"GEP3"})],
        }

        exptected_result = {
            "test_model": {
                "signal1": [{"GEP3_HEP7"}, {"VED4_GEN3"}],
                "signal2": [{"GEP3_HEP7"}],
            },
            "test_model2": {"sig1": [{"GEP3_HEP7"}, {"SPA"}], "sig2": [{"VED4_GEN3"}]},
            "test_model3": {"si1": [{"GEP3"}, {"VED4"}, {"GEP3"}]},
        }

        res = SignalInconsistency(TestSignalInconsistency._args)._merge_tuple_list(
            test_data
        )
        self.assertDictEqual(res, exptected_result)

    def test_aggregate_inports(self):
        """Test aggregate_inports"""
        per_unit_cfgs = {
            "GEP": {
                "VcAcCtrl": {
                    "inports": {
                        "TEST_SIG1": {},
                        "TEST_SIG2": {},
                        "VcAcCtrl.SIG_GEP": {},
                    }
                }
            },
            "VED": {
                "VcAcCtrl": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "SIG_VED": {}}
                },
                "MDL_VED": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "MDL_VED.SIG_VED": {}}
                },
            },
            "VEP": {
                "VcAcCtrl": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "UNIQUE_VEP": {}}
                },
                "MDL_VEP": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "MDL_VEP.SIG_VEP": {}}
                },
            },
        }

        expected_result = {
            "SIG_VED",
            "TEST_SIG1",
            "TEST_SIG2",
            "VcAcCtrl.SIG_GEP",
            "MDL_VED.SIG_VED",
            "MDL_VEP.SIG_VEP",
            "UNIQUE_VEP",
        }
        signal_inconsistency = SignalInconsistency(TestSignalInconsistency._args1)
        signal_inconsistency.per_unit_cfgs = per_unit_cfgs
        result = signal_inconsistency.aggregate_model_inports()
        self.assertEqual(expected_result, result)

    @patch("powertrain_build.signal_interfaces.CsvSignalInterfaces")
    def test_aggregate_supplier_inports(self, mock):
        """Test aggregate external outports"""
        mock_instance = mock.return_value

        def side_effect_get_external_outputs():
            out = {
                "EMS-Output": {"1sig1": {}, "1sig11": {}},
                "CAN-Output": {"1sig22": {}, "1sig23": {}},
            }
            return out

        mock_instance.get_external_outputs = MagicMock(
            side_effect=side_effect_get_external_outputs
        )

        signal_inconsistency = SignalInconsistency(TestSignalInconsistency._args1)
        signal_inconsistency.signal_ifs = {"prj1": mock_instance}

        result = signal_inconsistency.aggregate_supplier_inports()
        expected_result = {"1sig1", "1sig11", "1sig22", "1sig23"}
        self.assertEqual(result, expected_result)

    def test_check_unconsumed_files1(self):
        """Test exit code when all signals in unconsumed.csv is being consumed"""
        skip_all = {"mdl1": {"sig_1"}, "mdl2": {"sig_2", "sig_22"}, "mdl3": {"sig_3"}}
        TestSignalInconsistency._sig_incons.get_consumer_int = MagicMock(
            return_value=[("mdl1", "sig1")]
        )
        TestSignalInconsistency._sig_incons.get_consumer_ext = MagicMock(
            return_value=[("", "")]
        )
        TestSignalInconsistency._sig_incons.mdl_is_producer_in_prj = MagicMock(
            return_value=True
        )
        TestSignalInconsistency._sig_incons.fetch_signals_to_skip = MagicMock(
            return_value=skip_all
        )
        result, _ = TestSignalInconsistency._sig_incons.check_unconsumed_files(
            TestSignalInconsistency._used_inports, set()
        )
        self.assertEqual(result, EXIT_CODE_INCORRECT_CSV)
        TestSignalInconsistency._sig_incons.get_consumer_int.assert_called()
        TestSignalInconsistency._sig_incons.get_consumer_ext.assert_not_called()

    def test_check_unconsumed_files_2(self):
        """Test exit code when one signal in unconsumed.csv is being consumed"""
        skip_one = {"mdl1": {"sig_1"}}
        TestSignalInconsistency._sig_incons.get_consumer_int = MagicMock(
            return_value=[("mdl1", "sig1")]
        )
        TestSignalInconsistency._sig_incons.get_consumer_ext = MagicMock(
            return_value=[("", "")]
        )
        TestSignalInconsistency._sig_incons.mdl_is_producer_in_prj = MagicMock(
            return_value=True
        )
        TestSignalInconsistency._sig_incons.fetch_signals_to_skip = MagicMock(
            return_value=skip_one
        )
        result, _ = TestSignalInconsistency._sig_incons.check_unconsumed_files(
            TestSignalInconsistency._used_inports, set()
        )
        self.assertEqual(result, EXIT_CODE_INCORRECT_CSV)
        TestSignalInconsistency._sig_incons.get_consumer_ext.assert_not_called()

    def test_check_unconsumed_files_3(self):
        """Test exit code when unconsumed.csv files are empty"""
        TestSignalInconsistency._sig_incons.get_consumer_ext = MagicMock(
            return_value=[("", "")]
        )
        TestSignalInconsistency._sig_incons.fetch_signals_to_skip = MagicMock(
            return_value={}
        )
        result, _ = TestSignalInconsistency._sig_incons.check_unconsumed_files(
            TestSignalInconsistency._used_inports, set()
        )
        self.assertEqual(result, EXIT_CODE_OK)
        TestSignalInconsistency._sig_incons.get_consumer_ext.assert_not_called()

    def test_check_unconsumed_files_4(self):
        """Test exit code is returned if unconsumed.csv files are empty"""
        skip_none1 = {"mdl1": {"s"}, "mdl2": {"si", "sig"}, "mdl3": {"sig_"}}
        TestSignalInconsistency._sig_incons.get_consumer_ext = MagicMock(
            return_value=[("", "")]
        )
        TestSignalInconsistency._sig_incons.fetch_signals_to_skip = MagicMock(
            return_value=skip_none1
        )
        result, _ = TestSignalInconsistency._sig_incons.check_unconsumed_files(
            TestSignalInconsistency._used_inports, set()
        )
        self.assertEqual(result, EXIT_CODE_OK)
        TestSignalInconsistency._sig_incons.get_consumer_ext.assert_not_called()

    def test_check_unconsumed_files_5(self):
        """Test exit code only external signals"""
        used_ext_outports = {"sig1_ext", "sig2_ext", "sig3_ext"}
        signal_inconsistency1 = SignalInconsistency(TestSignalInconsistency._args1)
        signal_inconsistency1.mdl_is_producer_in_prj = MagicMock(return_value=True)
        signal_inconsistency1.fetch_signals_to_skip = MagicMock(
            return_value=TestSignalInconsistency._skip_all_ext
        )
        signal_inconsistency1.get_consumer_int = MagicMock(return_value=[("", "")])
        signal_inconsistency1.get_consumer_ext = MagicMock(return_value=[("", "")])
        result, _ = signal_inconsistency1.check_unconsumed_files(
            set(), used_ext_outports
        )
        self.assertEqual(result, EXIT_CODE_INCORRECT_CSV)
        signal_inconsistency1.get_consumer_int.assert_not_called()
        signal_inconsistency1.get_consumer_ext.assert_called()

    def test_check_unconsumed_files_6(self):
        """Test exit code no internal inports and no external outports"""
        signal_inconsistency2 = SignalInconsistency(TestSignalInconsistency._args1)
        signal_inconsistency2.get_consumer_int = MagicMock(return_value=[("", "")])
        signal_inconsistency2.get_consumer_ext = MagicMock(return_value=[("", "")])
        signal_inconsistency2.mdl_is_producer_in_prj = MagicMock(return_value=True)
        signal_inconsistency2.fetch_signals_to_skip = MagicMock(
            return_value=TestSignalInconsistency._skip_all_ext
        )
        result, _ = signal_inconsistency2.check_unconsumed_files(set(), set())
        self.assertEqual(result, EXIT_CODE_OK)
        signal_inconsistency2.get_consumer_int.assert_not_called()
        signal_inconsistency2.get_consumer_ext.assert_not_called()

    def test_get_consumer_int(self):
        """Test get consumer int"""
        per_unit_cfgs = {
            "GEP": {
                "VcAcCtrl": {
                    "inports": {
                        "TEST_SIG1": {},
                        "TEST_SIG2": {},
                        "VcAcCtrl.SIG_GEP": {},
                    }
                }
            },
            "VED": {
                "VcAcCtrl": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "SIG_VED": {}}
                },
                "MDL_VED": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "MDL_VED.SIG_VED": {}}
                },
            },
            "VEP": {
                "VcAcCtrl": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "UNIQUE_VEP": {}}
                },
                "MDL_VEP": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "MDL_VEP.SIG_VEP": {}}
                },
            },
        }

        signal_inconsistency = SignalInconsistency(TestSignalInconsistency._args1)
        signal_inconsistency.per_unit_cfgs = per_unit_cfgs
        result = signal_inconsistency.get_consumer_int("MDL_VEP.SIG_VEP")
        mdl, prj = result[0]  # list with tuples
        self.assertEqual(mdl, "MDL_VEP")
        self.assertEqual(prj, "VEP")

        expected_result = [
            ("VcAcCtrl", "GEP"),
            ("VcAcCtrl", "VED"),
            ("MDL_VED", "VED"),
            ("VcAcCtrl", "VEP"),
            ("MDL_VEP", "VEP"),
        ]
        result = signal_inconsistency.get_consumer_int("TEST_SIG2")
        self.assertEqual(result, expected_result)

    @patch("powertrain_build.signal_interfaces.CsvSignalInterfaces")
    def test_get_consumer_ext(self, mock):
        """Test aggregate external outports"""
        mock_instance = mock.return_value

        def side_effect_get_external_outputs(prj):
            out = {
                "prj1": {
                    "EMS-Output": {"1sig1": {}, "1sig11": {}},
                    "CAN-Output": {"1sig22": {}, "1sig23": {}},
                },
                "prj2": {
                    "LIN-Output": {"2sig1": {}, "2sig11": {}},
                    "CAN-Output": {"2sig22": {}, "2sig23": {}},
                },
                "prj3": {
                    "Private CAN-Output": {"1sig1": {}, "3sig11": {}},
                    "EMS-Output": {"3sig22": {}, "3sig23": {}},
                },
            }
            return out[prj]

        mock_instance.get_external_outputs = MagicMock(
            side_effect=side_effect_get_external_outputs
        )
        signal_inconsistency = SignalInconsistency(TestSignalInconsistency._args1)
        signal_inconsistency.signal_ifs = {
            "prj1": mock_instance,
            "prj2": mock_instance,
            "prj3": mock_instance,
        }
        result = signal_inconsistency.get_consumer_ext("1sig1")
        expected_result = [("EMS-Output", "prj1"), ("Private CAN-Output", "prj3")]
        self.assertEqual(result, expected_result)

    def test_mdl_is_producer_in_prj(self):
        """Test mdl is producing signal in project"""
        per_unit_cfgs = {
            "GEP": {
                "VcAcCtrl": {
                    "outports": {
                        "TEST_SIG1": {},
                        "TEST_SIG2": {},
                        "VcAcCtrl.SIG_GEP": {},
                    }
                }
            },
            "VED": {
                "VcAcCtrl": {
                    "outports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "SIG_VED": {}}
                },
                "MDL_VED": {
                    "outports": {
                        "TEST_SIG1": {},
                        "TEST_SIG2": {},
                        "MDL_VED.SIG_VED": {},
                    }
                },
            },
            "VEP": {
                "VcAcCtrl": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "UNIQUE_VEP": {}}
                },
                "MDL_VEP": {
                    "inports": {"TEST_SIG1": {}, "TEST_SIG2": {}, "MDL_VEP.SIG_VEP": {}}
                },
            },
        }

        signal_inconsistency = SignalInconsistency(TestSignalInconsistency._args1)
        signal_inconsistency.per_unit_cfgs = per_unit_cfgs
        # Model is producer
        result = signal_inconsistency.mdl_is_producer_in_prj(
            "VcAcCtrl", "VED", "TEST_SIG1"
        )
        self.assertEqual(result, True)

        # Model is not producer
        result = signal_inconsistency.mdl_is_producer_in_prj(
            "VcAcCtrl", "VED", "does_not_exist_signal"
        )
        self.assertEqual(result, False)

        # Model does not exist in project
        result = signal_inconsistency.mdl_is_producer_in_prj(
            "does_not_exist", "VED", "TEST_SIG1"
        )
        self.assertEqual(result, False)

        # Project does not exist
        result = signal_inconsistency.mdl_is_producer_in_prj(
            "VcAcCtrl", "does_not_exist_prj", "TEST_SIG1"
        )
        self.assertEqual(result, False)

        # Model does not have outports
        result = signal_inconsistency.mdl_is_producer_in_prj(
            "VcAcCtrl", "VEP", "TEST_SIG1"
        )
        self.assertEqual(result, False)

    def test_get_intersect_exit_code(self):
        """Test get_intersect_exit_code"""
        test_data = [("a", "a"), ("a", "b"), ("a", "c")]
        intersecting_signals = {"sig1", "sig2", "sig3"}
        self._sig_incons.get_consumer_int = MagicMock(return_value=test_data)
        self._sig_incons.get_consumer_ext = MagicMock(return_value=test_data)
        self._sig_incons.mdl_is_producer_in_prj = MagicMock(return_value=True)

        # Testing for internal signals fail.
        exit_code_int, _ = self._sig_incons.get_intersect_exit_code(
            "mdl", intersecting_signals
        )
        self.assertEqual(exit_code_int, EXIT_CODE_INCORRECT_CSV)

        # Testing for external signals fail.
        exit_code_ext, _ = self._sig_incons.get_intersect_exit_code(
            "mdl", intersecting_signals, False
        )
        self.assertEqual(exit_code_ext, EXIT_CODE_INCORRECT_CSV)

        self._sig_incons.mdl_is_producer_in_prj = MagicMock(return_value=False)
        # Testing for internal signals success.
        exit_code_int, _ = self._sig_incons.get_intersect_exit_code(
            "mdl", intersecting_signals
        )
        self.assertEqual(exit_code_int, EXIT_CODE_OK)

        # Testing for external signals success.
        exit_code_ext, _ = self._sig_incons.get_intersect_exit_code(
            "mdl", intersecting_signals, False
        )
        self.assertEqual(exit_code_ext, EXIT_CODE_OK)
