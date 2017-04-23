import json
from systemd import journal
import time

while True:
	entry = {
		"__REALTIME_TIMESTAMP" : str(time.time() * 1000),
		"_BOOT_ID" : "c84eb43384bf4c318d6b14a27ff8fe4b",
		"PRIORITY" : "6",
		"_PID" : "3670",
		"_UID" : "0",
		"_GID" : "0",
		"_COMM" : "self_test",
		"_EXE" : "/usr/bin/self_test",
		"_CMDLINE": "/usr/bin/self_test",
		"_CAP_EFFECTIVE" : "1fffffffff",
		"_SYSTEMD_CGROUP" : "/system.slice/docker.service",
		"_SYSTEMD_UNIT" : "self_test.service",
		"_SYSTEMD_SLICE" : "system.slice",
		"_MACHINE_ID" : "094e13ef7aba4afba796cad0697c19bf",
		"_HOSTNAME" : "localhost.localdomain",
		"_TRANSPORT" : "stdout",
		"SYSLOG_FACILITY" : "3",
		"SYSLOG_IDENTIFIER" : "journal-selftest-heartbeat",
		"_SELINUX_CONTEXT" : "system_u:system_r:init_t:s0",
		"MESSAGE": "self_test_journald_heartbeat"
	}

	journal.send(**entry)
	time.sleep(10)

