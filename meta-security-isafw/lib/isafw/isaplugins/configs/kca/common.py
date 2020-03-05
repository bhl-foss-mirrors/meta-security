############################################################################################
# Kernel Hardening Configurations
############################################################################################
hardening_kco = {'CONFIG_SERIAL_8250_CONSOLE': 'not set',
                 'CONFIG_SERIAL_CORE': 'not set',
                 'CONFIG_SERIAL_CORE_CONSOLE': 'not set',
                 'CONFIG_CMDLINE_BOOL': 'not set',
                 'CONFIG_CMDLINE': 'not set',
                 'CONFIG_CMDLINE_OVERRIDE': 'not set',
                 'CONFIG_DEBUG_INFO': 'not set',
                 'CONFIG_KGDB': 'not set',
                 'CONFIG_KPROBES': 'not set',
                 'CONFIG_FTRACE': 'not set',
                 'CONFIG_OPROFILE': 'not set',
                 'CONFIG_PROFILING': 'not set',
                 'CONFIG_MAGIC_SYSRQ': 'not set',
                 'CONFIG_DEBUG_BUGVERBOSE': 'not set',
                 'CONFIG_IP_PNP': 'not set',
                 'CONFIG_IKCONFIG': 'not set',
                 'CONFIG_SWAP': 'not set',
                 'CONFIG_NAMESPACES': 'not set',
                 'CONFIG_NFSD': 'not set',
                 'CONFIG_NFS_FS': 'not set',
                 'CONFIG_BINFMT_MISC': 'not set',
                 'CONFIG_KALLSYMS': 'not set',
                 'CONFIG_KALLSYMS_ALL': 'not set',
                 'CONFIG_BUG': 'not set',
                 'CONFIG_SYSCTL_SYSCALL': 'not set',
                 'CONFIG_MODULE_UNLOAD': 'not set',
                 'CONFIG_MODULE_FORCE_LOAD': 'not set',
                 'CONFIG_DEVMEM': 'not set',
                 'CONFIG_COREDUMP': 'not set',
                 'CONFIG_CROSS_MEMORY_ATTACH': 'not set',
                 'CONFIG_UNIX_DIAG': 'not set',
                 'CONFIG_CHECKPOINT_RESTORE': 'not set',
                 'CONFIG_PANIC_ON_OOPS': 'not set',
                 'CONFIG_PACKET_DIAG': 'not set',
                 'CONFIG_FW_LOADER_USER_HELPER': 'not set',
                 'CONFIG_BPF_JIT': 'not set',
                 'CONFIG_USELIB': 'not set',
                 'CONFIG_CC_STACKPROTECTOR': 'not set',
                 'CONFIG_KEXEC': 'not set',
                 'CONFIG_PROC_KCORE': 'not set',
                 'CONFIG_SECURITY_DMESG_RESTRICT': 'not set',
                 'CONFIG_DEBUG_STACKOVERFLOW': 'not set',
                 'CONFIG_DEBUG_STRICT_USER_COPY_CHECKS': 'not set',
                 'CONFIG_ARCH_HAS_DEBUG_STRICT_USER_COPY_CHECKS': 'not set',
                 'CONFIG_IKCONFIG_PROC': 'not set',
                 'CONFIG_RANDOMIZE_BASE': 'not set',
                 'CONFIG_DEBUG_RODATA': 'not set',
                 'CONFIG_STRICT_DEVMEM': 'not set',
                 'CONFIG_DEVKMEM': 'not set',
                 'CONFIG_ARCH_BINFMT_ELF_RANDOMIZE_PIE': 'not set',
                 'CONFIG_DEBUG_KERNEL': 'not set',
                 'CONFIG_DEBUG_FS': 'not set',
                 'CONFIG_MODULE_SIG_FORCE': 'not set',
                 }
hardening_kco_ref = {'CONFIG_SERIAL_8250_CONSOLE': 'not set',
                     'CONFIG_SERIAL_CORE': 'not set',
                     'CONFIG_SERIAL_CORE_CONSOLE': 'not set',
                     'CONFIG_CMDLINE_BOOL': 'y',
                     'CONFIG_CMDLINE': '"cmd_line"',
                     'CONFIG_CMDLINE_OVERRIDE': 'y',
                     'CONFIG_DEBUG_INFO': 'not set',
                     'CONFIG_KGDB': 'not set',
                     'CONFIG_KPROBES': 'not set',
                     'CONFIG_FTRACE': 'not set',
                     'CONFIG_OPROFILE': 'not set',
                     'CONFIG_PROFILING': 'not set',
                     'CONFIG_MAGIC_SYSRQ': 'not set',
                     'CONFIG_DEBUG_BUGVERBOSE': 'not set',
                     'CONFIG_IP_PNP': 'not set',
                     'CONFIG_IKCONFIG': 'not set',
                     'CONFIG_SWAP': 'not set',
                     'CONFIG_NAMESPACES': 'not set',
                     'CONFIG_NFSD': 'not set',
                     'CONFIG_NFS_FS': 'not set',
                     'CONFIG_BINFMT_MISC': 'not set',
                     'CONFIG_KALLSYMS': 'not set',
                     'CONFIG_KALLSYMS_ALL': 'not set',
                     'CONFIG_BUG': 'not set',
                     'CONFIG_SYSCTL_SYSCALL': 'not set',
                     'CONFIG_MODULE_UNLOAD': 'not set',
                     'CONFIG_MODULE_FORCE_LOAD': 'not set',
                     'CONFIG_DEVMEM': 'not set',
                     'CONFIG_COREDUMP': 'not set',
                     'CONFIG_CROSS_MEMORY_ATTACH': 'not set',
                     'CONFIG_UNIX_DIAG': 'not set',
                     'CONFIG_CHECKPOINT_RESTORE': 'not set',
                     'CONFIG_PANIC_ON_OOPS': 'y',
                     'CONFIG_PACKET_DIAG': 'not set',
                     'CONFIG_FW_LOADER_USER_HELPER': 'not set',
                     'CONFIG_BPF_JIT': 'not set',
                     'CONFIG_USELIB': 'not set',
                     'CONFIG_CC_STACKPROTECTOR': 'y',
                     'CONFIG_KEXEC': 'not set',
                     'CONFIG_PROC_KCORE': 'not set',
                     'CONFIG_SECURITY_DMESG_RESTRICT': 'y',
                     'CONFIG_DEBUG_STACKOVERFLOW': 'y',
                     'CONFIG_DEBUG_STRICT_USER_COPY_CHECKS': 'y',
                     'CONFIG_ARCH_HAS_DEBUG_STRICT_USER_COPY_CHECKS': 'y',
                     'CONFIG_IKCONFIG_PROC': 'not set',
                     'CONFIG_RANDOMIZE_BASE': 'y',
                     'CONFIG_DEBUG_RODATA': 'y',
                     'CONFIG_STRICT_DEVMEM': 'y',
                     'CONFIG_DEVKMEM': 'not set',
                     'CONFIG_ARCH_BINFMT_ELF_RANDOMIZE_PIE': 'y',
                     'CONFIG_DEBUG_KERNEL': 'not set',
                     'CONFIG_DEBUG_FS': 'not set',
                     'CONFIG_MODULE_SIG_FORCE': 'y',
                     }
############################################################################################
# Keys Kernel Configuration
############################################################################################
keys_kco = {'CONFIG_KEYS': 'not set',
            'CONFIG_TRUSTED_KEYS': 'not set',
            'CONFIG_ENCRYPTED_KEYS': 'not set',
            'CONFIG_KEYS_DEBUG_PROC_KEYS': 'not set'
            }
keys_kco_ref = {'CONFIG_KEYS': 'y',
                'CONFIG_TRUSTED_KEYS': 'y',
                'CONFIG_ENCRYPTED_KEYS': 'y',
                'CONFIG_KEYS_DEBUG_PROC_KEYS': 'not set'
                }
############################################################################################
# Security Kernel Configuration
############################################################################################
security_kco = {'CONFIG_SECURITY': 'not set',
                'CONFIG_SECURITYFS': 'not set',
                'CONFIG_SECURITY_NETWORKING': 'not set',
                'CONFIG_DEFAULT_SECURITY': 'not set',
                'CONFIG_SECURITY_SELINUX': 'not set',
                'CONFIG_SECURITY_SMACK': 'not set',
                'CONFIG_SECURITY_TOMOYO': 'not set',
                'CONFIG_SECURITY_APPARMOR': 'not set',
                'CONFIG_SECURITY_YAMA': 'not set',
                'CONFIG_SECURITY_YAMA_STACKED': 'not set'
                }
security_kco_ref = {'CONFIG_SECURITY': 'y',
                    'CONFIG_SECURITYFS': 'y',
                    'CONFIG_SECURITY_NETWORKING': 'y',
                    'CONFIG_DEFAULT_SECURITY': '"selinux","smack","apparmor","tomoyo"',
                    'CONFIG_SECURITY_SELINUX': 'y',
                    'CONFIG_SECURITY_SMACK': 'y',
                    'CONFIG_SECURITY_TOMOYO': 'y',
                    'CONFIG_SECURITY_APPARMOR': 'y',
                    'CONFIG_SECURITY_YAMA': 'y',
                    'CONFIG_SECURITY_YAMA_STACKED': 'y'
                    }
############################################################################################
# Integrity Kernel Configuration
############################################################################################
integrity_kco = {'CONFIG_INTEGRITY': 'not set',
                 'CONFIG_INTEGRITY_SIGNATURE': 'not set',
                 'CONFIG_INTEGRITY_AUDIT': 'not set',
                 'CONFIG_IMA': 'not set',
                 'CONFIG_IMA_LSM_RULES': 'not set',
                 'CONFIG_IMA_APPRAISE': 'not set',
                 'CONFIG_IMA_TRUSTED_KEYRING': 'not set',
                 'CONFIG_IMA_APPRAISE_SIGNED_INIT': 'not set',
                 'CONFIG_EVM': 'not set',
                 'CONFIG_EVM_ATTR_FSUUID': 'not set',
                 'CONFIG_EVM_EXTRA_SMACK_XATTRS': 'not set',
                 'CONFIG_IMA_DEFAULT_HASH_SHA1': 'not set',
                 'CONFIG_IMA_DEFAULT_HASH_SHA256': 'not set',
                 'CONFIG_IMA_DEFAULT_HASH_SHA512': 'not set',
                 'CONFIG_IMA_DEFAULT_HASH_WP512': 'not set'
                 }
integrity_kco_ref = {'CONFIG_INTEGRITY': 'y',
                     'CONFIG_INTEGRITY_SIGNATURE': 'y',
                     'CONFIG_INTEGRITY_AUDIT': 'y',
                     'CONFIG_IMA': 'y',
                     'CONFIG_IMA_LSM_RULES': 'y',
                     'CONFIG_IMA_APPRAISE': 'y',
                     'CONFIG_IMA_TRUSTED_KEYRING': 'y',
                     'CONFIG_IMA_APPRAISE_SIGNED_INIT': 'y',
                     'CONFIG_EVM': 'y',
                     'CONFIG_EVM_ATTR_FSUUID': 'y',
                     'CONFIG_EVM_EXTRA_SMACK_XATTRS': 'y',
                     'CONFIG_IMA_DEFAULT_HASH_SHA1': 'not set',
                     'CONFIG_IMA_DEFAULT_HASH_SHA256': 'y',
                     'CONFIG_IMA_DEFAULT_HASH_SHA512': 'y',
                     'CONFIG_IMA_DEFAULT_HASH_WP512': 'not set'
                     }
############################################################################################
# Comments
############################################################################################
comments = {  # Kernel Hardening Configurations
    'CONFIG_SERIAL_8250_CONSOLE': 'Enables the serial console. Providing access to the serial console would assist an attacker in discovering attack vectors.',
    'CONFIG_SERIAL_CORE': 'Enables the serial console. Providing access to the serial console would assist an attacker in discovering attack vectors.',
    'CONFIG_SERIAL_CORE_CONSOLE': 'Enables the serial console. Providing access to the serial console would assist an attacker in discovering attack vectors.',
    'CONFIG_CMDLINE_BOOL': 'Enables the kernel command line to be hardcoded directly into the kernel. Hardcoding the command line allows tighter control over kernel command line options.',
    'CONFIG_CMDLINE': 'Defines the kernel command line to be hardcoded into the kernel. Hardcoding the command line allows tighter control over kernel command line options.',
    'CONFIG_CMDLINE_OVERRIDE': 'Enables the kernel to ignore the boot loader command line and to use only the hardcoded command line. Hardcoding the command line allows tighter control over kernel command line options.',
    'CONFIG_DEBUG_INFO': 'Enables debug symbols in the kernel. Providing debug symbols would assist an attacker in discovering attack vectors.',
    'CONFIG_KGDB': 'Enables KGDB over USB and console ports. Providing KGDB would assist an attacker in discovering attack vectors.',
    'CONFIG_KPROBES': 'Enables Kernel Dynamic Probes. Providing kprobes allows the attacker to collect debug and performance information.',
    'CONFIG_FTRACE': 'Enables the kernel to trace every function. Providing kernel trace functionality would assist an attacker in discovering attack vectors.',
    'CONFIG_OPROFILE': 'Enables a profiling system capable of profiling kernel and kernel modules. Providing profiling functionality would assist an attacker in discovering attack vectors.',
    'CONFIG_PROFILING': 'Enables a profiling system capable of profiling kernel and kernel modules. Providing profiling functionality would assist an attacker in discovering attack vectors.',
    'CONFIG_MAGIC_SYSRQ': 'Enables a console device to interpret special characters as SysRQ system commands. SysRQ commands are an immediate attack vector as they provide the ability to dump information or reboot the device.',
    'CONFIG_DEBUG_BUGVERBOSE': 'Enables verbose logging for BUG() panics. Verbose logging would assist an attacker in discovering attack vectors.',
    'CONFIG_IP_PNP': 'Enables automatic configuration of IP addresses of devices and of the routing table during kernel boot. Providing networking functionality before the system has come up would assist an attacker in discovering attack vectors.',
    'CONFIG_IKCONFIG': 'Enables access to the kernel config through /proc/config.gz. Leaking the kernel configuration would assist an attacker in discovering attack vectors.',
    'CONFIG_SWAP': 'Enables swap files for kernel. The ability to read kernel memory pages in swap files would assist an attacker in discovering attack vectors.',
    'CONFIG_NAMESPACES': 'Enabling this can result in duplicates of dev nodes, pids and mount points, which can be useful to attackers trying to spoof running environments on devices.',
    'CONFIG_NFSD': 'Enables remote access to files residing on this system using Sun\'s Network File System protocol. Providing remote access to the file system would assist an attacker in discovering attack vectors.',
    'CONFIG_NFS_FS': 'Enables remote access to files residing on this system using Sun\'s Network File System protocol. Providing remote access to the file system would assist an attacker in discovering attack vectors.',
    'CONFIG_BINFMT_MISC': 'Enables support for binary formats other than ELF. Providing the ability to use alternate interpreters would assist an attacker in discovering attack vectors.',
    'CONFIG_KALLSYMS': 'Enables printing of symbolic crash information and symbolic stack backtraces. Verbose logging would assist an attacker in discovering attack vectors.',
    'CONFIG_KALLSYMS_ALL': 'Enables printing of symbolic crash information and symbolic stack backtraces. Verbose logging would assist an attacker in discovering attack vectors.',
    'CONFIG_BUG': 'Enables display of backtrace and register information for BUGs and WARNs in kernel space. Verbose logging would assist an attacker in discovering attack vectors.',
    'CONFIG_SYSCTL_SYSCALL': 'Enables sysctl to read and write kernel parameters. Use of deprecated and unmaintained features is not recommended.',
    'CONFIG_MODULE_UNLOAD': 'Enables the ability to unload a kernel module. Allowing module unloading enables the attacker to disable security modules.',
    'CONFIG_MODULE_FORCE_LOAD': 'Enables forced loading of modules without version information. Providing an attacker with the ability to force load a module assists in discovering attack vectors.',
    'CONFIG_DEVMEM': 'Enables mem device, which provides access to physical memory. Providing a view into physical memory would assist an attacker in discovering attack vectors.',
    'CONFIG_COREDUMP': 'Enables support for performing core dumps. Providing core dumps would assist an attacker in discovering attack vectors.',
    'CONFIG_CROSS_MEMORY_ATTACH': 'Enables cross-process virtual memory access. Providing virtual memory access to and from a hostile process would assist an attacker in discovering attack vectors.',
    'CONFIG_UNIX_DIAG': 'Enables support for socket monitoring interface. Allows the attacker to inspect shared file descriptors on Unix Domain sockets or traffic on \'localhost\'.',
    'CONFIG_CHECKPOINT_RESTORE': 'Enables the checkpoint/restore service which can freeze and migrate processes. Providing a method for manipulating process state would assist an attacker in discovering attack vectors.',
    'CONFIG_PANIC_ON_OOPS': 'Enables conversion of kernel OOPs to PANIC. When fuzzing the kernel or attempting kernel exploits, attackers are likely to trigger kernel OOPSes. Setting the behavior on OOPS to PANIC can impede their progress.',
    'CONFIG_PACKET_DIAG': 'Enables support for socket monitoring interface. Allows the attacker to inspect shared file descriptors on Unix Domain sockets or traffic on \'localhost\'.',
    'CONFIG_FW_LOADER_USER_HELPER': 'Enables the invocation of user-helper (e.g. udev) for loading firmware files as a fallback after the direct file loading in kernel fails. Providing firmware auto loader functionality would assist an attacker in discovering attack vectors.',
    'CONFIG_BPF_JIT': 'Enables Berkeley Packet Filter filtering capabilities. The BPF JIT can be used to create kernel-payloads from firewall table rules which assist an attacker in discovering attack vectors.',
    'CONFIG_USELIB': 'Enables the uselib syscall. The uselib system call has no valid use in any libc6 or uclibc system. Legacy features would assist an attacker in discovering attack vectors.',
    'CONFIG_CC_STACKPROTECTOR': 'Enables the stack protector GCC feature which defends against stack-based buffer overflows',
    'CONFIG_KEXEC': 'Enables the ability to shutdown your current kernel, and start another one. If enabled, this can be used as a way to bypass signed kernels.',
    'CONFIG_PROC_KCORE': 'Enables access to a kernel core dump from userspace. Providing access to core dumps of the kernel would assist an attacker in discovering attack vectors.',
    'CONFIG_SECURITY_DMESG_RESTRICT': 'Enables restrictions on unprivileged users reading the kernel syslog via dmesg(8). Unrestricted access to kernel syslogs would assist an attacker in discovering attack vectors.',
    'CONFIG_DEBUG_STACKOVERFLOW': 'Enables messages to be printed if free stack space drops below a certain limit. Leaking information about resources used by the kernel would assist an attacker in discovering attack vectors.',
    'CONFIG_DEBUG_STRICT_USER_COPY_CHECKS': 'Converts a certain set of sanity checks for user copy operations into compile time failures. The copy_from_user() etc checks help test if there are sufficient security checks on the length argument of the copy operation by having gcc prove that the argument is within bounds.',
    'CONFIG_ARCH_HAS_DEBUG_STRICT_USER_COPY_CHECKS': 'Required to enable DEBUG_STRICT_USER_COPY_CHECKS, but alone does not provide security.',
    'CONFIG_IKCONFIG_PROC': 'Enables access to the kernel config through /proc/config.gz. Leaking the kernel configuration would assist an attacker in discovering attack vectors.',
    'CONFIG_RANDOMIZE_BASE': 'Enables Kernel Address Space Layout randomization (kASLR). This hinders some types of security attacks by making it more difficult for an attacker to predict target addresses.',
    'CONFIG_DEBUG_RODATA': 'Sets kernel text and rodata sections as read-only and write-protected. This guards against malicious attempts to change the kernel\'s executable code.',
    'CONFIG_STRICT_DEVMEM': 'Enables restriction of userspace access to kernel memory. Failure to enable this option provides an immediate attack vector.',
    'CONFIG_DEVKMEM': 'Enables kmem device, which direct maps kernel memory. Providing a view into kernel memory would assist an attacker in discovering attack vectors.',
    'CONFIG_ARCH_BINFMT_ELF_RANDOMIZE_PIE': 'Enables randomization of PIE load address  for ELF binaries. This hinders some types of security attacks by making it more difficult for an attacker to predict target addresses.',
    'CONFIG_DEBUG_KERNEL': 'Enables sysfs output intended to assist with debugging a kernel. The information output to sysfs would assist an attacker in discovering attack vectors.',
    'CONFIG_DEBUG_FS': 'Enables the kernel debug filesystem. The kernel debug filesystem presents a lot of useful information and means of manipulation of the kernel to an attacker.',
    'CONFIG_MODULE_SIG_FORCE': 'Enables validation of module signature. Disabling this option enables an attacker to load unsigned modules.',
}