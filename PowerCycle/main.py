import sys, getopt
from get_func import *
import subprocess
import safe_reboot

upperbound = 3
count = 0

# def main(argv):
wait("Press any key to stop...", 5)

file_name = get_filepath("power_cycle_log.txt")
file_name = "/root/Desktop/PowerCycle/power_cycle_log.txt"

# upperbound = get_upperbound()
curr_count = get_count(file_name)
wait("...", 10)
if curr_count >= upperbound:
	go_finish(file_name, curr_count)
	msgBox(curr_count)
else:
	action_list_for_log = ["date", "echo do sth~", "free"]
	add_log(curr_count, action_list_for_log, file_name)

	go_reboot(file_name)


# if __name__ == "__main__":
#    main(sys.argv[1:])
