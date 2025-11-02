from deepmerge import Merger
import copy
import json

# 合併規則：list 用 append，dict 用 merge，其他型別用 override
# override
# merge
# append / prepend
# append_unique / prepend_unique

merger = Merger(
    [(list, ["append"]), (dict, ["merge"])], # (type, [strategy_name]) 列表
    ["override"], # 當沒有匹配 type 時使用的策略
    ["override"]  # 當 type 不是 list/dict 時的策略
)

dic_main = {
    "name": "pump pa10vo",
    "name_en": "PA10VO Series axial piston pump",
    "name_tw": "PA10VO系列柱塞泵",
    "name_zh": "PA10VO系列柱塞泵",
    "supply_default_value": "s",
    "option_item_count": 12,
    "models_order": [
        "01un",
        "02md",
        "03dp",
        "04ct",
        "05sr",
        "06cr",
        "07se",
        "08axv",
        "09ln",
        "10dn",
        "11th",
        "12sd"
    ],
    "main_model": "04ct",
    "select_way": 1,
    "models": {
        "01un": {
            "name_en": "Axial piston unit",
            "name_tw": "軸向柱塞單元",
            "name_zh": "轴向柱塞单元",
            "postfix_symbol": "",
            "default_value": "PA10V",
            "model_item_length": 5,
            "model_items_order": [
                "PA10V"
            ],
            "model_items": {
                "PA10V": {
                    "item_name_en": "Swashplate design, variable",
                    "item_name_tw": "斜盤設計，變量泵",
                    "item_name_zh": "斜盘设计，变量泵",
                    "supply": "s"
                }
            }
        },
        "02md": {
            "name_en": "Mounting",
            "name_tw": "裝配方式",
            "name_zh": "装配方式",
            "postfix_symbol": "",
            "default_value": "O",
            "model_item_length": 1,
            "model_items_order": [
                "O"
            ],
            "model_items": {
                "O": {
                    "item_name_en": "Pump, open circuit",
                    "item_name_tw": "泵，開式回路",
                    "item_name_zh": "泵，开式回路",
                    "supply": "s"
                }
            }
        },
        "03dp": {
            "name_en": "Size",
            "name_tw": "排量規格",
            "name_zh": "排量规格",
            "postfix_symbol": "",
            "default_value": "",
            "model_item_length": 3,
            "model_items_order": [
                "010",
                "018",
                "028",
                "045",
                "060",
                "063",
                "085",
                "100"
            ],
            "model_items": {
                "010": {
                    "item_name_en": "10cm³/rev",
                    "item_name_tw": "10cm³/rev",
                    "item_name_zh": "10cm³/rev",
                    "supply": "s"
                },
                "018": {
                    "item_name_en": "18cm³/rev",
                    "item_name_tw": "18cm³/rev",
                    "item_name_zh": "18cm³/rev",
                    "supply": "n"
                },
                "028": {
                    "item_name_en": "28cm³/rev",
                    "item_name_tw": "28cm³/rev",
                    "item_name_zh": "28cm³/rev",
                    "supply": "n"
                },
                "045": {
                    "item_name_en": "45cm³/rev",
                    "item_name_tw": "45cm³/rev",
                    "item_name_zh": "45cm³/rev",
                    "supply": "n"
                },
                "060": {
                    "item_name_en": "60cm³/rev",
                    "item_name_tw": "60cm³/rev",
                    "item_name_zh": "60cm³/rev",
                    "supply": "s"
                },
                "063": {
                    "item_name_en": "63cm³/rev",
                    "item_name_tw": "63cm³/rev",
                    "item_name_zh": "63cm³/rev",
                    "supply": "s"
                },
                "085": {
                    "item_name_en": "85cm³/rev",
                    "item_name_tw": "85cm³/rev",
                    "item_name_zh": "85cm³/rev",
                    "supply": "n"
                },
                "100": {
                    "item_name_en": "100cm³/rev",
                    "item_name_tw": "100cm³/rev",
                    "item_name_zh": "100cm³/rev",
                    "supply": "n"
                }
            }
        }
    },
    "uid": "dbdcedbe-7bde-4b2c-8cfb-b21e8ccde68d"
}


dic_a = {
    "models": {
        "03dp": {
            "model_items": {
                "010": {
                    "alias": "10"
                    },
                "018": {
                    "alias": "18"
                    },
            }
        }
    }
}
# print(json.dumps(dic_main, indent=4, ensure_ascii=False))
# print(json.dumps(dic_a, indent=4, ensure_ascii=False))


combined_data = copy.deepcopy(dic_main)
merger.merge(combined_data, dic_a)
print('result: ')
print(json.dumps(combined_data, indent=4, ensure_ascii=False))