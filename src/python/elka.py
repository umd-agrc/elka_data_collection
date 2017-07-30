# Generated by h2py from src/elka_comm/common/elka.h

# Included from time.h
_TIME_H = 1

# Included from features.h
_FEATURES_H = 1
_ISOC95_SOURCE = 1
_ISOC99_SOURCE = 1
_ISOC11_SOURCE = 1
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 200809L
_XOPEN_SOURCE = 700
_XOPEN_SOURCE_EXTENDED = 1
_LARGEFILE64_SOURCE = 1
_DEFAULT_SOURCE = 1
_BSD_SOURCE = 1
_SVID_SOURCE = 1
_ATFILE_SOURCE = 1
_DEFAULT_SOURCE = 1
_BSD_SOURCE = 1
_SVID_SOURCE = 1
__USE_ISOC11 = 1
__USE_ISOC99 = 1
__USE_ISOC95 = 1
__USE_ISOCXX11 = 1
__USE_POSIX_IMPLICITLY = 1
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 200809L
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 2
_POSIX_C_SOURCE = 199506L
_POSIX_C_SOURCE = 200112L
_POSIX_C_SOURCE = 200809L
__USE_POSIX_IMPLICITLY = 1
__USE_POSIX = 1
__USE_POSIX2 = 1
__USE_POSIX199309 = 1
__USE_POSIX199506 = 1
__USE_XOPEN2K = 1
__USE_ISOC95 = 1
__USE_ISOC99 = 1
__USE_XOPEN2K8 = 1
_ATFILE_SOURCE = 1
__USE_XOPEN = 1
__USE_XOPEN_EXTENDED = 1
__USE_UNIX98 = 1
_LARGEFILE_SOURCE = 1
__USE_XOPEN2K8 = 1
__USE_XOPEN2K8XSI = 1
__USE_XOPEN2K = 1
__USE_XOPEN2KXSI = 1
__USE_ISOC95 = 1
__USE_ISOC99 = 1
__USE_XOPEN_EXTENDED = 1
__USE_LARGEFILE = 1
__USE_LARGEFILE64 = 1
__USE_FILE_OFFSET64 = 1
__USE_MISC = 1
__USE_BSD = 1
__USE_SVID = 1
__USE_ATFILE = 1
__USE_GNU = 1
__USE_REENTRANT = 1
__USE_FORTIFY_LEVEL = 2
__USE_FORTIFY_LEVEL = 1
__USE_FORTIFY_LEVEL = 0
__GNU_LIBRARY__ = 6
__GLIBC__ = 2
__GLIBC_MINOR__ = 19

# Included from sys/cdefs.h
_SYS_CDEFS_H = 1
def __NTH(fct): return fct

def __NTH(fct): return fct

def __P(args): return args

def __PMT(args): return args

def __STRING(x): return #x

def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1)

def __bos0(ptr): return __builtin_object_size (ptr, 0)

def __warnattr(msg): return __attribute__((__warning__ (msg)))

__flexarr = []
__flexarr = [0]
__flexarr = []
__flexarr = [1]
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname)

def __attribute__(xyz): return  

def __attribute_alloc_size__(params): return \

def __attribute_alloc_size__(params): return  

def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x)))

def __attribute_format_arg__(x): return  

def __glibc_unlikely(cond): return __builtin_expect ((cond), 0)

def __glibc_likely(cond): return __builtin_expect ((cond), 1)

def __glibc_unlikely(cond): return (cond)

def __glibc_likely(cond): return (cond)


# Included from bits/wordsize.h
__WORDSIZE = 64
__WORDSIZE = 32
__WORDSIZE_TIME64_COMPAT32 = 1
__SYSCALL_WORDSIZE = 64
__LDBL_COMPAT = 1
def __LDBL_REDIR_DECL(name): return \

__USE_LARGEFILE = 1
__USE_LARGEFILE64 = 1
__USE_EXTERN_INLINES = 1

# Included from gnu/stubs.h

# Included from bits/time.h
_STRUCT_TIMEVAL = 1

# Included from bits/types.h
_BITS_TYPES_H = 1
__S32_TYPE = int
__SWORD_TYPE = int
__SLONG32_TYPE = int

# Included from bits/typesizes.h
_BITS_TYPESIZES_H = 1
__FSWORD_T_TYPE = __SWORD_TYPE
__PID_T_TYPE = __S32_TYPE
__DADDR_T_TYPE = __S32_TYPE
__KEY_T_TYPE = __S32_TYPE
__CLOCKID_T_TYPE = __S32_TYPE
__SSIZE_T_TYPE = __SWORD_TYPE
__OFF_T_MATCHES_OFF64_T = 1
__INO_T_MATCHES_INO64_T = 1
__FD_SETSIZE = 1024
_BITS_TIME_H = 1
CLOCKS_PER_SEC = 1000000l
CLOCK_REALTIME = 0
CLOCK_MONOTONIC = 1
CLOCK_PROCESS_CPUTIME_ID = 2
CLOCK_THREAD_CPUTIME_ID = 3
CLOCK_MONOTONIC_RAW = 4
CLOCK_REALTIME_COARSE = 5
CLOCK_MONOTONIC_COARSE = 6
CLOCK_BOOTTIME = 7
CLOCK_REALTIME_ALARM = 8
CLOCK_BOOTTIME_ALARM = 9
TIMER_ABSTIME = 1

# Included from bits/timex.h
_BITS_TIMEX_H = 1
ADJ_OFFSET = 0x0001
ADJ_FREQUENCY = 0x0002
ADJ_MAXERROR = 0x0004
ADJ_ESTERROR = 0x0008
ADJ_STATUS = 0x0010
ADJ_TIMECONST = 0x0020
ADJ_TAI = 0x0080
ADJ_MICRO = 0x1000
ADJ_NANO = 0x2000
ADJ_TICK = 0x4000
ADJ_OFFSET_SINGLESHOT = 0x8001
ADJ_OFFSET_SS_READ = 0xa001
MOD_OFFSET = ADJ_OFFSET
MOD_FREQUENCY = ADJ_FREQUENCY
MOD_MAXERROR = ADJ_MAXERROR
MOD_ESTERROR = ADJ_ESTERROR
MOD_STATUS = ADJ_STATUS
MOD_TIMECONST = ADJ_TIMECONST
MOD_CLKB = ADJ_TICK
MOD_CLKA = ADJ_OFFSET_SINGLESHOT
MOD_TAI = ADJ_TAI
MOD_MICRO = ADJ_MICRO
MOD_NANO = ADJ_NANO
STA_PLL = 0x0001
STA_PPSFREQ = 0x0002
STA_PPSTIME = 0x0004
STA_FLL = 0x0008
STA_INS = 0x0010
STA_DEL = 0x0020
STA_UNSYNC = 0x0040
STA_FREQHOLD = 0x0080
STA_PPSSIGNAL = 0x0100
STA_PPSJITTER = 0x0200
STA_PPSWANDER = 0x0400
STA_PPSERROR = 0x0800
STA_CLOCKERR = 0x1000
STA_NANO = 0x2000
STA_MODE = 0x4000
STA_CLK = 0x8000
STA_RONLY = (STA_PPSSIGNAL | STA_PPSJITTER | STA_PPSWANDER | \
    STA_PPSERROR | STA_CLOCKERR | STA_NANO | STA_MODE | STA_CLK)
CLK_TCK = CLOCKS_PER_SEC
__clock_t_defined = 1
__time_t_defined = 1
__clockid_t_defined = 1
__timer_t_defined = 1
__timespec_defined = 1
TIME_UTC = 1

# Included from xlocale.h
_XLOCALE_H = 1
def __isleap(year): return \


# Included from stdint.h
_STDINT_H = 1

# Included from bits/wchar.h
_BITS_WCHAR_H = 1
def __INT64_C(c): return c ## L

def __UINT64_C(c): return c ## UL

def __INT64_C(c): return c ## LL

def __UINT64_C(c): return c ## ULL

INT8_MIN = (-128)
INT16_MIN = (-32767-1)
INT32_MIN = (-2147483647-1)
INT64_MIN = (-__INT64_C(9223372036854775807)-1)
INT8_MAX = (127)
INT16_MAX = (32767)
INT32_MAX = (2147483647)
INT64_MAX = (__INT64_C(9223372036854775807))
UINT8_MAX = (255)
UINT16_MAX = (65535)
UINT64_MAX = (__UINT64_C(18446744073709551615))
INT_LEAST8_MIN = (-128)
INT_LEAST16_MIN = (-32767-1)
INT_LEAST32_MIN = (-2147483647-1)
INT_LEAST64_MIN = (-__INT64_C(9223372036854775807)-1)
INT_LEAST8_MAX = (127)
INT_LEAST16_MAX = (32767)
INT_LEAST32_MAX = (2147483647)
INT_LEAST64_MAX = (__INT64_C(9223372036854775807))
UINT_LEAST8_MAX = (255)
UINT_LEAST16_MAX = (65535)
UINT_LEAST64_MAX = (__UINT64_C(18446744073709551615))
INT_FAST8_MIN = (-128)
INT_FAST16_MIN = (-9223372036854775807L-1)
INT_FAST32_MIN = (-9223372036854775807L-1)
INT_FAST16_MIN = (-2147483647-1)
INT_FAST32_MIN = (-2147483647-1)
INT_FAST64_MIN = (-__INT64_C(9223372036854775807)-1)
INT_FAST8_MAX = (127)
INT_FAST16_MAX = (9223372036854775807L)
INT_FAST32_MAX = (9223372036854775807L)
INT_FAST16_MAX = (2147483647)
INT_FAST32_MAX = (2147483647)
INT_FAST64_MAX = (__INT64_C(9223372036854775807))
UINT_FAST8_MAX = (255)
UINT_FAST64_MAX = (__UINT64_C(18446744073709551615))
INTPTR_MIN = (-9223372036854775807L-1)
INTPTR_MAX = (9223372036854775807L)
INTPTR_MIN = (-2147483647-1)
INTPTR_MAX = (2147483647)
INTMAX_MIN = (-__INT64_C(9223372036854775807)-1)
INTMAX_MAX = (__INT64_C(9223372036854775807))
UINTMAX_MAX = (__UINT64_C(18446744073709551615))
PTRDIFF_MIN = (-9223372036854775807L-1)
PTRDIFF_MAX = (9223372036854775807L)
PTRDIFF_MIN = (-2147483647-1)
PTRDIFF_MAX = (2147483647)
SIG_ATOMIC_MIN = (-2147483647-1)
SIG_ATOMIC_MAX = (2147483647)
def INT8_C(c): return c

def INT16_C(c): return c

def INT32_C(c): return c

def INT64_C(c): return c ## L

def INT64_C(c): return c ## LL

def UINT8_C(c): return c

def UINT16_C(c): return c

def UINT32_C(c): return c ## U

def UINT64_C(c): return c ## UL

def UINT64_C(c): return c ## ULL

def INTMAX_C(c): return c ## L

def UINTMAX_C(c): return c ## UL

def INTMAX_C(c): return c ## LL

def UINTMAX_C(c): return c ## ULL


# Included from inttypes.h
_INTTYPES_H = 1
____gwchar_t_defined = 1
__PRI64_PREFIX = "l"
__PRIPTR_PREFIX = "l"
__PRI64_PREFIX = "ll"
PRId8 = "d"
PRId16 = "d"
PRId32 = "d"
PRIdLEAST8 = "d"
PRIdLEAST16 = "d"
PRIdLEAST32 = "d"
PRIdFAST8 = "d"
PRIi8 = "i"
PRIi16 = "i"
PRIi32 = "i"
PRIiLEAST8 = "i"
PRIiLEAST16 = "i"
PRIiLEAST32 = "i"
PRIiFAST8 = "i"
PRIo8 = "o"
PRIo16 = "o"
PRIo32 = "o"
PRIoLEAST8 = "o"
PRIoLEAST16 = "o"
PRIoLEAST32 = "o"
PRIoFAST8 = "o"
PRIu8 = "u"
PRIu16 = "u"
PRIu32 = "u"
PRIuLEAST8 = "u"
PRIuLEAST16 = "u"
PRIuLEAST32 = "u"
PRIuFAST8 = "u"
PRIx8 = "x"
PRIx16 = "x"
PRIx32 = "x"
PRIxLEAST8 = "x"
PRIxLEAST16 = "x"
PRIxLEAST32 = "x"
PRIxFAST8 = "x"
PRIX8 = "X"
PRIX16 = "X"
PRIX32 = "X"
PRIXLEAST8 = "X"
PRIXLEAST16 = "X"
PRIXLEAST32 = "X"
PRIXFAST8 = "X"
SCNd8 = "hhd"
SCNd16 = "hd"
SCNd32 = "d"
SCNdLEAST8 = "hhd"
SCNdLEAST16 = "hd"
SCNdLEAST32 = "d"
SCNdFAST8 = "hhd"
SCNi8 = "hhi"
SCNi16 = "hi"
SCNi32 = "i"
SCNiLEAST8 = "hhi"
SCNiLEAST16 = "hi"
SCNiLEAST32 = "i"
SCNiFAST8 = "hhi"
SCNu8 = "hhu"
SCNu16 = "hu"
SCNu32 = "u"
SCNuLEAST8 = "hhu"
SCNuLEAST16 = "hu"
SCNuLEAST32 = "u"
SCNuFAST8 = "hhu"
SCNo8 = "hho"
SCNo16 = "ho"
SCNo32 = "o"
SCNoLEAST8 = "hho"
SCNoLEAST16 = "ho"
SCNoLEAST32 = "o"
SCNoFAST8 = "hho"
SCNx8 = "hhx"
SCNx16 = "hx"
SCNx32 = "x"
SCNxLEAST8 = "hhx"
SCNxLEAST16 = "hx"
SCNxLEAST32 = "x"
SCNxFAST8 = "hhx"
MAX_ELKA_DEVS = 2
MAX_SERIAL_PORTS = 6
MAX_NAME_LEN = 80
MSG_NUM_LEN = 0xffff
RECENT_ACKS_LEN = 0xff
MAX_MSG_LEN = 0xff
NO_BUF = 0
ARRAY = 3
PRIORITY_QUEUE = 4
PRDIT = PRIu16
PRDPT = PRIu8
UINT16_MAX = 0xffff
ID_MAX = UINT16_MAX
PORT_NUM = 0xe0
PORT_TYPE = 0x1c
PROC_SIDE = 0x03
PORT_NONE = 0x00
PORT_UART = 0x01
PORT_WIFI = 0x02
PORT_RADIO = 0x03
POSIX_SIDE = 0x00
QURT_SIDE = 0x01
ELKA_SIDE = 0x02
SENDER_ID = (-281474976710656)
RECEIVER_ID = 0xffff00000000
SENDER_PARAMS = 0xff000000
RECEIVER_PARAMS = 0xff0000
MESSAGE_TYPE = 0xff00
MESSAGE_LENGTH = 0xff
ID_EXPECTING_ACK = 0x0100
TYPE_EXPECTING_ACK = 0x01
PyBROADCAST_MSG_ID = 0x00
MSG_NULL = 0x00
MSG_ACCEPTED = 0x02
MSG_DENIED = 0x04
MSG_UNSUPPORTED = 0x06
MSG_FAILED = 0x08
MSG_MOTOR_CMD = 0x0a
MSG_ACK = 0x0c
MSG_ROUTE_DEV_PROPS = 0x0e
MSG_ROUTE_REQUEST_HB = 0x10
MSG_ROUTE_HB = 0x12
MSG_PORT_CTL = 0x03
MSG_ELKA_CTL = 0x05
MSG_ROUTE_CHANGED = 0x07
MSG_ROUTE_TABLE = 0x09
MSG_ACK_LENGTH = 1
MSG_STATE_LENGTH = 1
MAX_NUM_RETRIES = 21
HW_CTL_NULL = 0x00
HW_CTL_FAILED = 0x01
HW_CTL_KILL = 0x02
HW_CTL_START = 0x03
HW_CTL_STOP = 0x04
HW_CTL_PAUSE = 0x05
HW_CTL_RESUME = 0x06
SW_CTL_NULL = 0x00
SW_CTL_FAILED = 0x01
SW_CTL_KILL = 0x02
SW_CTL_REMOTE = 0x03
SW_CTL_SPEKTRUM = 0x04
SW_CTL_AUTOPILOT = 0x05
PyDEV_PROP_POSIX_SIDE = 0x00
PyDEV_PROP_QURT_SIDE = 0x01
PyDEV_PROP_ELKA_SIDE = 0x02
PyDEV_PROP_HW_CONNECTED = 0x03
PyDEV_PROP_WIRELESS_CONNECTED = 0x04
PyDEV_PROP_GROUND_STATION = 0x05
PyDEV_PROP_FLIGHT_CONTROLLER = 0x06
PyDEV_PROP_PERFORM_LOCALIZATION = 0x07
PyDEV_PROP_SENSE_LOCATION = 0x08
PyDEV_PROP_HAS_MOTORS = 0x0a
PyDEV_PROP_USE_CAMERA = 0x0b
PyDEV_PROP_HAS_CAMERA = 0x0c
PyDEV_PROP_TRANSMISSION_CTL = 0x0d
SPEKTRUM_STICK_RANGE = 21
SPEKTRUM_STICK_LOW = 1099
SPEKTRUM_STICK_MID = 1500
SPEKTRUM_STICK_HIGH = 1901
SPEKTRUM_SWITCH_LOW = 1099
SPEKTRUM_SWITCH_MID = 1500
SPEKTRUM_SWITCH_HIGH = 1901
CONNECTION_ERROR = -1
CONNECTION_NULL = 0
CONNECTION_CLOSED = 1
CONNECTION_OPEN = 2