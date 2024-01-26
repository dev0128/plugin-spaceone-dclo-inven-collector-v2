_METADATA = {
    "view": {
        "search": [
            {"key": "data.code", "name": "Code"},
            {"key": "data.name", "name": "Name"},
            {
                "key": "data.category",
                "name": "Category",
            },
            {
                "key": "data.report_lv",
                "name": "Severity",
                "enums": [
                    "High",
                    "Medium",
                    "Low",
                ],
            },
            {
                "key": "data.flag",
                "name": "Result",
                "enums": [
                    "Secure",
                    "Vuln",
                    "N/A",
                ],
            },
        ],
        "table": {
            "layout": {
                "name": "",
                "type": "query-search-table",
                "options": {
                    "default_sort": {"key": "data.code", "desc": False},
                    "fields": [
                        {
                            "type": "text",
                            "key": "data.code",
                            "name": "Rule ID",
                        },
                        {
                            "type": "enum",
                            "key": "data.category",
                            "name": "Category",
                        },
                        {
                            "type": "text",
                            "key": "data.name",
                            "name": "Rule Name",
                        },
                        {
                            "type": "enum",
                            "key": "data.report_lv",
                            "name": "Severity",
                            "options": {
                                "High": {
                                    "type": "badge",
                                    "options": {"background_color": "#ff5344"},
                                },
                                "Medium": {
                                    "type": "badge",
                                    "options": {"background_color": "#ffa726"},
                                },
                                "Low": {
                                    "type": "badge",
                                    "options": {"background_color": "#f7d959"},
                                },
                            },
                        },
                        {
                            "type": "text",
                            "key": "data.findings_cnt",
                            "name": "Findings",
                        },
                        {
                            "type": "enum",
                            "key": "data.flag",
                            "name": "Result",
                            "options": {
                                "Vuln": {
                                    "type": "badge",
                                    "options": {"background_color": "coral.500"},
                                },
                                "Secure": {
                                    "type": "badge",
                                    "options": {"background_color": "indigo.500"},
                                },
                                "N/A": {
                                    "type": "badge",
                                    "options": {"background_color": "dimgray.500"},
                                },
                            },
                        },
                    ],
                },
            },
        },
        "widget": [
            {
                "name": "High",
                "type": "summary",
                "options": {
                    "value_options": {"key": "value", "options": {"default": 0}}
                },
                "query": {
                    "aggregate": [{"count": {"name": "value"}}],
                    "filter": [
                        {"key": "data.report_lv", "value": "High", "operator": "eq"},
                        {"key": "data.flag", "value": "Vuln", "operator": "eq"},
                    ],
                },
            },
            {
                "name": "Medium",
                "type": "summary",
                "options": {
                    "value_options": {"key": "value", "options": {"default": 0}}
                },
                "query": {
                    "aggregate": [{"count": {"name": "value"}}],
                    "filter": [
                        {"key": "data.report_lv", "value": "Medium", "operator": "eq"},
                        {"key": "data.flag", "value": "Vuln", "operator": "eq"},
                    ],
                },
            },
            {
                "name": "Low",
                "type": "summary",
                "options": {
                    "value_options": {"key": "value", "options": {"default": 0}}
                },
                "query": {
                    "aggregate": [{"count": {"name": "value"}}],
                    "filter": [
                        {"key": "data.report_lv", "value": "Low", "operator": "eq"},
                        {"key": "data.flag", "value": "Vuln", "operator": "eq"},
                    ],
                },
            },
            {
                "name": "Secure",
                "type": "summary",
                "options": {
                    "value_options": {"key": "value", "options": {"default": 0}}
                },
                "query": {
                    "aggregate": [{"count": {"name": "value"}}],
                    "filter": [
                        {"key": "data.flag", "value": "Secure", "operator": "eq"},
                    ],
                },
            },
            {
                "name": "N/A",
                "type": "summary",
                "options": {
                    "value_options": {"key": "value", "options": {"default": 0}}
                },
                "query": {
                    "aggregate": [{"count": {"name": "value"}}],
                    "filter": [
                        {"key": "data.flag", "value": "N/A", "operator": "eq"},
                    ],
                },
            },
        ],
        "sub_data": {
            "layouts": [
                {
                    "type": "item",
                    "name": "교정 세부정보",
                    "options": {
                        "fields": [
                            {"type": "text", "key": "code", "name": "Rule ID"},
                            {
                                "type": "text",
                                "key": "name",
                                "name": "Rule Name",
                            },
                            {
                                "type": "text",
                                "key": "category",
                                "name": "Category",
                            },
                            {
                                "type": "enum",
                                "key": "report_lv",
                                "name": "Severity",
                                "options": {
                                    "High": {
                                        "type": "badge",
                                        "options": {"background_color": "#ff5344"},
                                    },
                                    "Medium": {
                                        "type": "badge",
                                        "options": {"background_color": "#ffa726"},
                                    },
                                    "Low": {
                                        "type": "badge",
                                        "options": {"background_color": "#f7d959"},
                                    },
                                },
                            },
                            {
                                "type": "text",
                                "key": "compliance_decs",
                                "name": "Description",
                            },
                            {
                                "type": "text",
                                "key": "rule_standard",
                                "name": "Assessment Criteria",
                            },
                            {
                                "type": "text",
                                "key": "action_plan",
                                "name": "Mitigation Plan",
                            },
                        ],
                        "root_path": "data",
                    },
                },
                {
                    "type": "table",
                    "name": "Compliance",
                    "options": {
                        "fields": [
                            {
                                "type": "text",
                                "key": "com_1",
                                "name": "Major",
                                # "options": {
                                #     "outline_color": "violet.500"
                                # },
                            },
                            {
                                "type": "text",
                                "key": "com_2",
                                "name": "Sub",
                                # "options": {
                                #     "outline_color": "violet.500"
                                # },
                            },
                            {
                                "type": "text",
                                "key": "com_3",
                                "name": "Subclass",
                                # "options": {
                                #     "outline_color": "violet.500"
                                # },
                            },
                        ],
                        "root_path": "data.compliance_dtl",
                    },
                },
                {
                    "type": "table",
                    "name": "Vulnerable List",
                    "options": {
                        "fields": [
                            {"type": "text", "key": "region", "name": "Region"},
                            {"type": "text", "key": "id", "name": "Resource ID"},
                            {"type": "text", "key": "name", "name": "Resource Name"},
                            {
                                "type": "text",
                                "key": "resource_type",
                                "name": "Resource Type",
                            },
                            {
                                "type": "more",
                                "key": "detail",
                                "name": "Vulnerable findings",
                                "options": {
                                    "sub_key": "popup_data",
                                    "layout": {
                                        "name": "Vulnerable Status",
                                        "type": "popup",
                                        "options": {
                                            "layout": {
                                                "type": "raw",
                                            }
                                        },
                                    },
                                },
                            },
                        ],
                        "root_path": "data.flag_key",
                    },
                },
                {
                    "type": "table",
                    "name": "Secure List",
                    "options": {
                        "fields": [
                            {"type": "text", "key": "region", "name": "Region"},
                            {"type": "text", "key": "id", "name": "Resource ID"},
                            {"type": "text", "key": "name", "name": "Resource Name"},
                            {
                                "type": "text",
                                "key": "resource_type",
                                "name": "Resource Type",
                            },
                            {
                                "type": "more",
                                "key": "detail",
                                "name": "Secure findings",
                                "options": {
                                    "sub_key": "popup_data",
                                    "layout": {
                                        "name": "Secure Status",
                                        "type": "popup",
                                        "options": {
                                            "layout": {
                                                "type": "raw",
                                            }
                                        },
                                    },
                                },
                            },
                        ],
                        "root_path": "data.good_key",
                    },
                },
            ]
        },
    }
}
