from package import *

cols = """duration,
protocol_type,
service,
flag,
src_bytes,
dst_bytes,
land,
wrong_fragment,
urgent,
hot,
num_failed_logins,
logged_in,
num_compromised,
root_shell,
su_attempted,
num_root,
num_file_creations,
num_shells,
num_access_files,
num_outbound_cmds,
is_host_login,
is_guest_login,
count,
srv_count,
serror_rate,
srv_serror_rate,
rerror_rate,
srv_rerror_rate,
same_srv_rate,
diff_srv_rate,
srv_diff_host_rate,
dst_host_count,
dst_host_srv_count,
dst_host_same_srv_rate,
dst_host_diff_srv_rate,
dst_host_same_src_port_rate,
dst_host_srv_diff_host_rate,
dst_host_serror_rate,
dst_host_srv_serror_rate,
dst_host_rerror_rate,
dst_host_srv_rerror_rate"""

columns = [c.strip() for c in cols.split(',') if c.strip()]


attacks_types = {
    'normal': 'normal',
    'back': 'dos', 'neptune': 'dos', 'smurf': 'dos', 'teardrop': 'dos', 'land': 'dos', 'pod': 'dos', 'apache2': 'dos',
    'mailbomb': 'dos', 'processtable': 'dos', 'udpstorm': 'dos',
    'satan': 'probe', 'portsweep': 'probe', 'ipsweep': 'probe', 'nmap': 'probe', 'mscan': 'probe', 'saint': 'probe',
    'warezmaster': 'r2l', 'warezclient': 'r2l', 'ftp_write': 'r2l', 'guess_passwd': 'r2l', 'imap': 'r2l',
    'multihop': 'r2l', 'phf': 'r2l', 'spy': 'r2l', 'sendmail': 'r2l', 'named': 'r2l', 'snmpgetattack': 'r2l',
    'snmpguess': 'r2l', 'xlock': 'r2l', 'xsnoop': 'r2l', 'worm': 'r2l',
    'rootkit': 'u2r', 'buffer_overflow': 'u2r', 'loadmodule': 'u2r', 'perl': 'u2r', 'httptunnel': 'u2r', 'ps': 'u2r',
    'sqlattack': 'u2r', 'xterm': 'u2r'
}


def get_pre_file_data(file_name):
    df = pd.read_csv(file_name, names=columns)

    protocol_map = {'icmp': 0, 'tcp': 1, 'udp': 2}
    flag_map = {'SF': 0, 'S0': 1, 'REJ': 2, 'RSTR': 3, 'RSTO': 4, 'SH': 5, 'S1': 6, 'S2': 7, 'RSTOS0': 8, 'S3': 9,
                'OTH': 10}
    service_map = {'aol': 0, 'auth': 1, 'bgp': 2, 'courier': 3, 'csnet_ns': 4, 'ctf': 5, 'daytime': 6, 'discard': 7,
                   'domain': 8, 'domain_u': 9, 'echo': 10, 'eco_i': 11, 'ecr_i': 12, 'efs': 13, 'exec': 14,
                   'finger': 15,
                   'ftp': 16, 'ftp_data': 17, 'gopher': 18, 'harvest': 19, 'hostnames': 20, 'http': 21, 'http_2784': 22,
                   'http_443': 23, 'http_8001': 24, 'imap4': 25, 'IRC': 26, 'iso_tsap': 27, 'klogin': 28, 'kshell': 29,
                   'ldap': 30, 'link': 31, 'login': 32, 'mtp': 33, 'name': 34, 'netbios_dgm': 35, 'netbios_ns': 36,
                   'netbios_ssn': 37, 'netstat': 38, 'nnsp': 39, 'nntp': 40, 'ntp_u': 41, 'other': 42, 'pm_dump': 43,
                   'pop_2': 44, 'pop_3': 45, 'printer': 46, 'private': 47, 'red_i': 48, 'remote_job': 49, 'rje': 50,
                   'shell': 51, 'smtp': 52, 'sql_net': 53, 'ssh': 54, 'sunrpc': 55, 'supdup': 56, 'systat': 57,
                   'telnet': 58,
                   'tftp_u': 59, 'tim_i': 60, 'time': 61, 'urh_i': 62, 'urp_i': 63, 'uucp': 64, 'uucp_path': 65,
                   'vmnet': 66,
                   'whois': 67, 'X11': 68, 'Z39_50': 69}

    df['protocol_type'] = df['protocol_type'].map(protocol_map)
    df['flag'] = df['flag'].map(flag_map)
    df['service'] = df['service'].map(service_map)

    return df


def Pre_Handle_Data(file_name, columns):
    df = pd.read_csv(file_name, names=columns)

    df.drop('num_root', axis=1, inplace=True)
    df.drop('srv_serror_rate', axis=1, inplace=True)
    df.drop('srv_rerror_rate', axis=1, inplace=True)
    df.drop('dst_host_srv_serror_rate', axis=1, inplace=True)
    df.drop('dst_host_serror_rate', axis=1, inplace=True)
    df.drop('dst_host_rerror_rate', axis=1, inplace=True)
    df.drop('dst_host_srv_rerror_rate', axis=1, inplace=True)
    df.drop('dst_host_same_srv_rate', axis=1, inplace=True)
    df.drop('is_host_login', axis=1, inplace=True)
    df.drop('is_guest_login', axis=1, inplace=True)
    df = df.dropna(axis=1, how='any')

    protocol_map = {'icmp': 0, 'tcp': 1, 'udp': 2}
    flag_map = {'SF': 0, 'S0': 1, 'REJ': 2, 'RSTR': 3, 'RSTO': 4, 'SH': 5, 'S1': 6, 'S2': 7, 'RSTOS0': 8, 'S3': 9,
                'OTH': 10}
    service_map = {'aol': 0, 'auth': 1, 'bgp': 2, 'courier': 3, 'csnet_ns': 4, 'ctf': 5, 'daytime': 6, 'discard': 7,
                   'domain': 8, 'domain_u': 9, 'echo': 10, 'eco_i': 11, 'ecr_i': 12, 'efs': 13, 'exec': 14,
                   'finger': 15,
                   'ftp': 16, 'ftp_data': 17, 'gopher': 18, 'harvest': 19, 'hostnames': 20, 'http': 21, 'http_2784': 22,
                   'http_443': 23, 'http_8001': 24, 'imap4': 25, 'IRC': 26, 'iso_tsap': 27, 'klogin': 28, 'kshell': 29,
                   'ldap': 30, 'link': 31, 'login': 32, 'mtp': 33, 'name': 34, 'netbios_dgm': 35, 'netbios_ns': 36,
                   'netbios_ssn': 37, 'netstat': 38, 'nnsp': 39, 'nntp': 40, 'ntp_u': 41, 'other': 42, 'pm_dump': 43,
                   'pop_2': 44, 'pop_3': 45, 'printer': 46, 'private': 47, 'red_i': 48, 'remote_job': 49, 'rje': 50,
                   'shell': 51, 'smtp': 52, 'sql_net': 53, 'ssh': 54, 'sunrpc': 55, 'supdup': 56, 'systat': 57,
                   'telnet': 58,
                   'tftp_u': 59, 'tim_i': 60, 'time': 61, 'urh_i': 62, 'urp_i': 63, 'uucp': 64, 'uucp_path': 65,
                   'vmnet': 66,
                   'whois': 67, 'X11': 68, 'Z39_50': 69}

    df['protocol_type'] = df['protocol_type'].map(protocol_map)
    df['flag'] = df['flag'].map(flag_map)
    df['service'] = df['service'].map(service_map)

    df.drop('service', axis=1, inplace=True)

    return df
