import pathlib
import shutil


def main() -> None:
    source = pathlib.Path(r"modfiles")
    target = pathlib.Path(r"C:\Games\Standalone\Factorio FPTest\mods\factoryplanner_1.2.0")
    # target = pathlib.Path(r"C:\Games\Standalone\Factorio\mods\factoryplanner_1.2.0")

    shutil.copytree(source, target, dirs_exist_ok=True)


if __name__ == '__main__':
    main()
