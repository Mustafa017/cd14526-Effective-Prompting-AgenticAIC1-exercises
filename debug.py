import re

docstring = """Compute the area of a circle.
 
    Args:
        radius (int): The radius of the circle (must be non-negative).
        unit (str): Unit of measurement (default: "cm"). Accepts "cm" or "m".
 
    Returns:
        float: Area of the circle in the specified unit.
"""


def tool_eval(tool_desc:str) -> dict[str, str]:
    tool_args: dict[str, str] = {}

    ARGS_RETURNS_REGEX = r'(?:\s*Args:\s*([\s\S]*?))?(?:\s*Returns:\s*([\s\S]*?))?$'
    if re.search(ARGS_RETURNS_REGEX, tool_desc):
        # args, returns = re.search(ARGS_RETURNS_REGEX, tool_desc).groups()
        args = re.search(ARGS_RETURNS_REGEX, tool_desc).groups()[0]
        print(args)
        # PARAMS_DESC_REGEX = r"(\w+):\s*(.*?)(?=\n\s*\w+:|$)"
        PARAMS_DESC_REGEX = r"(\w+)\s*\((.*?)\):\s*(.*?)(?=\n\s*\w+\s*\(.*?\):|$)"

        for index, value in enumerate(re.findall(PARAMS_DESC_REGEX, args), start=1):
            tool_args[f"args{index}"] = value[0]
    return tool_args

# ************************* Notebook script****************
# def tool_eval(tool_fn) -> dict[str, Any]:
    tool_dict: dict[str, Any] = {}
    tool_dict["tool_name"] = tool_fn.__name__
    tool_desc = get_tool_descriptions_string([tool_fn])
    # print(tool_desc)
    
    def _get_tool_args(tool_desc:str) -> dict[str, str]:
        tool_args: dict[str, str] = {}

        ARGS_RETURNS_REGEX = r'(?:\s*Args:\s*([\s\S]*?))?(?:\s*Returns:\s*([\s\S]*?))?$'
        # args, returns = re.search(ARGS_RETURNS_REGEX, tool_desc).groups()
        args = re.search(ARGS_RETURNS_REGEX, tool_desc).groups()[0]

        if args:
            PARAMS_DESC_REGEX = r"(\w+)\s*\((.*?)\):\s*(.*?)(?=\n\s*\w+\s*\(.*?\):|$)"

            for index, value in enumerate(re.findall(PARAMS_DESC_REGEX, args), start=1):
                tool_args[f"args{index}"] = value[0]
        return tool_args
    
    tool_dict["arguments"] = _get_tool_args(tool_desc)
    return tool_dict


# for tool_func in ALL_TOOLS:
    print(tool_eval(tool_func))


if __name__ == "__main__":
    print(tool_eval(docstring))

