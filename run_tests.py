import argparse
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description="Orchestrator for vHIL Robotics Framework")
    parser.add_argument("--scenario", help="Select scenario to test (e.g., 'sensor', 'navigation', 'critical')")
    parser.add_argument("--mode", help="Execution mode (e.g., 'full', 'unit', 'integration', 'sensors')")
    
    args = parser.parse_args()
    
    cmd = [sys.executable, "-m", "pytest"]
    
    if args.scenario:
        print(f"Running scenario marked with: {args.scenario}")
        cmd.extend(["-m", args.scenario])
    elif args.mode:
        if args.mode == "full":
            print("Running full test suite")
        elif args.mode in ["unit", "integration", "sensors"]:
            print(f"Running {args.mode} tests")
            cmd.append(f"tests/{args.mode}/")
        else:
            print(f"Unknown mode: {args.mode}")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)
        
    print(f"Executing: {' '.join(cmd)}")
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
