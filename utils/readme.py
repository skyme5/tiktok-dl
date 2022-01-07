import subprocess

with open("utils/template.rst", "r") as f:
    content = f.read()

with open("README.rst", "w") as file:

    def strip_empty(e):
        if len(e) == 0:
            return e
        return "    " + e

    cmd_out = subprocess.run(
        ["venv/Scripts/python.exe", "tiktok_dl\\cli.py", "--help"],
        stdout=subprocess.PIPE,
    )
    args = [strip_empty(i) for i in cmd_out.stdout.decode("utf-8").split("\n")]
    file.write(content.replace("{{COMMAND_ARGS}}", "".join(args)))
