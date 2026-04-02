"""Test whether Tk's wm iconbitmap hangs on macOS.

https://github.com/python/cpython/issues/146531
"""

import platform
import shutil
import subprocess
import sys

TIMEOUT = 60


def test_wish_iconbitmap():
    """Test wm iconbitmap via wish (pure Tk, no Python)."""
    print(f"Platform: {platform.platform()}")
    print(f"Python: {sys.version}")

    wish = shutil.which("wish")
    if not wish:
        print("SKIP: wish not found")
        return
    print(f"wish path: {wish}")

    # Get Tk version via tclsh (wish may hang on macOS)
    tclsh = shutil.which("tclsh")
    if tclsh:
        result = subprocess.run(
            [tclsh],
            input="puts [info patchlevel]; exit",
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
        )
        print(f"Tcl version: {result.stdout.strip()}")

    # Test: wm iconbitmap . hourglass
    print("\nTest: wm iconbitmap . hourglass (wish)")
    print(f"Running with {TIMEOUT}s timeout...")
    script = 'wm iconbitmap . hourglass\nputs "OK: wm iconbitmap succeeded"\nexit\n'
    try:
        result = subprocess.run(
            [wish],
            input=script,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
        )
        print(f"stdout: {result.stdout.strip()}")
        print(f"stderr: {result.stderr.strip()}")
        print(f"returncode: {result.returncode}")
    except subprocess.TimeoutExpired:
        sys.exit(f"HUNG: wish wm iconbitmap timed out after {TIMEOUT}s!")


if __name__ == "__main__":
    test_wish_iconbitmap()
