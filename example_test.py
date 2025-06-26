import subprocess
import shlex
import sys


def main() -> None:
    checkpoints = r".\checkpoints"
    cmd = (
        "python test.py "
        "--dataroot ./datasets/PseudoClean "
        "--name PseudoClean "
        "--model cycle_gan "
        "--netG resnet_9blocks "
        "--netD basic "
        "--input_nc 1 "
        "--output_nc 1 "
        "--gpu_ids 0 "
        "--num_test 100 "
        "--results_dir ./results/PseudoClean "
        f'--checkpoints_dir "{checkpoints}" '
        "--epoch latest"
    )

    print("Running:\n", cmd, "\n")
    res = subprocess.run(shlex.split(cmd), check=True)

    print("\nFinished with exit code:", res.returncode)

if __name__ == "__main__":
    sys.exit(main())
