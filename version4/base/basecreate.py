#!/usr/bin/python
import sqlite3

class DataBase:
	pass

def create_tables():
	data_version = [('5', '^(\$.*?(\s=|\s=\s|=\s|=)mysql_.*?)|((\smysql_|mysql_).*)$', 'extenssion mysql'),
                    	('7', '^declare.?strict_types(\s=|=\s|\s=\s|=)1.*?$', 'scalar type declarations mode strict'),
                    	('7', '^(\$.*?(\s=|=\s|\s=\s|=).*?(\s\?\?\s.*?)+)$', 'operator ?? null'),
                    	('4', '(mcrypt_(cbc|cfb|ecb|ofb)(\(([\"\w\s\S\"]*)\)))', 'Encrypts/decrypts data in CBC|CFB|ECB|OFB mode'),
			('4','^(.*?ereg.*?)$','extension ereg'),
			('4','^(\$.*?(\s=|\s=\s|=\s|=)mssql_.*?)|((\smssql_|mssql_).*)$','extension mssql'),
			('4','^(\$.*?(\s=|\s=\s|=\s|=)sybase_.*?)|((\ssybase_|sybase_).*)$','extension sybase'),
			('7','^function\s.*?((((int|float|bool|string)\s\$.*?)(,(int|float|bool|string)\s\$.*?)*)|(\$.*?(,\$.*?)*)):(int|float|bool|string).*?$','return type declarations'),
			('7','^(function\s.*?((int|float|bool|string)\s\$.*?)(,(int|float|bool|string)\s\$.*?)*)$','scalar type declarations mode coercive'),
			('7','(.*?\s<=>.*?)$','operator <=>'),
			('4','(call_user_method((\(([\"\w\s\S\"]*)\))|_array(\(([\"\w\s\S\"]*)\))))','Call a user method on an specific object'),
			('4','(define_syslog_variables(\(([\"\w\s\S\"]*)\)))','Initializes all syslog related variables'),
			('4','(dl(\(([\"\w\s\S\"]*)\)))','Loads a PHP extension at runtime'),
			('4','(mcrypt_generic_end(\(([\"\w\s\S\"]*)\)))','This function terminates encryption'),
			('4','(set_magic_quotes_runtime(\(([\"\w\s\S\"]*)\)))','Sets the current active configuration setting of magic_quotes_runtime'),
			('4','(session_(register|unregister|is_registered)(\(([\"\w\s\S\"]*)\)))','Register one or more global variables with the current session'),
			('4','(set_socket_blocking)(\(([\"\w\s\S\"]*)\))','Set blocking/non-blocking mode on a stream'),
			('4','(split(|i))(\(([\"\w\s\S\"]*)\))','Split string into array by regular expression'),
			('4','(sql_regcase(\(([\"\w\s\S\"]*)\)))','Make regular expression for case insensitive match'),
			('4','(mysql_db_query(\(([\"\w\s\S\"]*)\)))','Selects a database and executes a query on it'),
			('4','(mysql_escape_string(\(([\"\w\s\S\"]*)\)))','Escapes a string for use in a mysql_query'),
			('4','(mysql_list_dbs(\(([\"\w\s\S\"]*)\)))','List databases available on a MySQL server'),
			('5','(IntlDateFormatter\:\:setTimeZoneID(\(([\"\w\s\S\"]*)\)))','Sets the time zone to use'),
			('5','(datefmt_set_timezone_set(\(([\"\w\s\S\"]*)\)))','Sets the time zone to use')]
	data_recommendation = [('https://diego.com.es/ataques-xss-cross-site-scripting-en-php', 'xss'),
			       ('http://wonko.com/post/html-escaping', 'xss'),
			       ('https://www.codeproject.com/Articles/134024/HTML-and-JavaScript-Injection', 'xss'),
			       ('http://resources.infosecinstitute.com/file-inclusion-attacks/', 'LFI & RFI'),
			       ('https://www.netsparker.com/blog/web-security/remote-file-inclusion-vulnerability/', 'LFI' ),
			       ('http://resources.infosecinstitute.com/php-lab-file-inclusion-attacks/', 'LFI & RFI'),
			       ('https://www.htbridge.com/vulnerability/php-file-inclusion.html', 'RFI'),
			       ('https://www.esecurityplanet.com/browser-security/how-to-prevent-remote-file-inclusion-rfi-attacks.html', 'RFI'),
			       ('http://phpsecurity.readthedocs.io/en/latest/Injection-Attacks.html', 'RFI'),
			       ('https://www.cyberciti.biz/faq/linux-unix-apache-lighttpd-phpini-disable-functions/', 'RFI'),
			       ('https://www.incapsula.com/web-application-security/rfi-remote-file-inclusion.html', 'RFI'),
			       ('https://www.drupal.org/node/2068441', 'RFI'),
			       ('https://secure.php.net/manual/en/language.types.string.php#language.types.string.syntax.single', 'RFI'),
			       ('https://www.owasp.org/index.php/Injection_Prevention_Cheat_Sheet', 'ci'),
			       ('https://www.owasp.org/index.php/PHP_Security_Cheat_Sheet#Cookies', 'sc'),
			       ('http://phpsecurity.readthedocs.io/en/latest/Injection-Attacks.html#command-injection', 'pt')]
	data_function = [('mysql_db_query', 'mysql_db_query(\s\(|\()\s(.*?|\$.*?)\s,\s(.*?|\$.*?)\s,\s\$.*?(\s\)|\));', 'mysqli_select_db()', 'obsoleta en PHP 5.3.0', '1'),
			 ('mysql_select_db', 'mysql_select_db(\s\(|\().*?', 'mysqli_select_db()', 'obsoleta en PHP 5.5.0 y eliminada en PHP 7.0.0', '1'),
			 ('sql_regcase', 'sql_regcase(\s\(|\().*?(\s\)|\));', 'preg_quote() y/o preg_match()', 'OBSOLETA en PHP 5.3.0', '1'),
			 ('mcrypt_generic_end', 'mcrypt_generic_end(\s\(|\()\s(.*?|\$.*?)(\s\)|\))', 'mcrypt_generic_deinit()', 'OBSOLETA en PHP 5.3.0', '1'),
			 ('ereg', 'ereg(\s\(|\().*?(\s\)|\))', 'preg_match()', 'OBSOLETA en PHP 5.3.0', '1'),
			 ('call_user_method', 'call_user_method(\s\(|\().*?(\s\)|\))', 'call_user_func()', ' OBSOLETA en PHP 4.1.0', '4'),
		   	 ('mcrypt_cbc y/o mcrypt_cfb y/o mcrypt_ecb y/o mcrypt_ofb', '(mcrypt_(cbc|cfb|ecb|ofb)(\(([\"\w\s\S\"]*)\)))', 'mcrypt_decrypt() o mcrypt_encrypt()', 'OBSOLETA en PHP 5.5.0', '1'),
			 ('mysql_()', '^(\$.*?(\s=|\s=\s|=\s|=)mysql_.*?)|((\smysql_|mysql_).*)$', 'mysqli_()', 'OBSOLETA en PHP 5.3.0', '1')]
	data_name_vul = [('sqli',' '),('xss', ' '),('sc', ' '),('send', ' '),('lfi&rfi', ' '),('pt', ' '),('ci', ' '),('ifc', ' ')]
	data_vulnerability = [('2', '(?<!(trim\())(\$\_(POST|REQUEST|GET)\[.*\])', 'global variables that do not start with the function trim', '1'),
			      ('2', '(?<!(strip\_tags\())(\$\_(POST|REQUEST|GET)\[.*\])', 'global variables that do not start with the function strip_tags ', '1'),
			      ('2', '(?<!(htmlspecialchars\())(\$\_(POST|REQUEST|GET)\[.*\])', 'global variables that do not start with the function htmlespecialchars', '1'),
			      ('2', '(?<!(htmlentities\())(\$\_(POST|REQUEST|GET)\[.*\])', 'global variables that do not start with the function htmlentities', '1'),
                              ('2', '>.*?<\s*\/?[\w\s]+>', 'Unquoted HTML breaking with closing tag', '2'),
			      ('2', '[\"\'].*?>', 'HTML breaking', '2'),
		     	      ('2', '<base\b.+?\bhref\b.+?>', 'Common JavaScript injection points (forms)', '3'),
			      ('2', '\bon\w+\s*=', 'HTML event handler', '3'),
			      ('5', '(?<!(include\s))(\$\_(POST|REQUEST|GET)\[.*\])', 'Critical PHP function include', '4'),
			      ('5', '\.\.[\/\\]', 'Directory traversal', '5'),
			      ('5', '%2e%2e[\/\\]', 'Directory traversal urlencoding', '5'),
			      ('5', '%c0%ae[\/\\]', 'Directory traversal urlencoding', '5'),
			      ('5', '\.(ht(access|passwd|group))|(apache|httpd)\d?\.conf', 'Directory traversal', '5'),
			      ('5', '\/etc\/[.\/]*(passwd|shadow|master\.passwd)', 'Directory traversal', '5'),
                              ('5', '%\w+%', 'Windows environment variable pattern', '6'),
                              ('5', '(?<!\w)(boot\.ini|global\.asa|sam)\b', 'Common Windows files', '6'),
                              ('5', '\bfile_(get|put)_contents\b.*?\(.+?\)', 'Critical PHP function file_get_contents/file_put_contents', '6'),
		              ('5', '\breadfile\b.*?\(.+?\)', 'Critical PHP function readfile', '4'),
                              ('5', '\binclude(_once)?\b.*?;', 'Critical PHP function include', '4'),
                              ('5', '\brequire(_once)?\b.*?;', 'Critical PHP function require', '4'),
			      ('5', '\(\)\s*\{.*?;\s*\}\s*;', 'Shellshock (CVE-2014-6271)', '6'),
     			      ('5', '(\b(do|while|for)\b.*?\([^)]*\).*?\{)|(\}.*?\b(do|while|for)\b.*?\([^)]*\))', 'C-style loops', '6'),
                              ('5', '[=(].+?\?.+?\:', 'C-style ternary operator', '6'),
                              ('5', '\\u00[a-f0-9]{2}', 'Octal entity', '7'),
                              ('5', '\\x0*[a-f0-9]{2}', 'Hex entity', '7'),
                              ('5', '<\?(?!xml\s)', 'PHP opening tag', '9'),
                              ('5', '\/\/input', 'PHP input stream', '8'),
                              ('5', '\bcall_user_func\b.*?\(.+?\)', 'Critical PHP function call_user_func', '10'),
                              ('5', '\bcreate_function\b.*?\(.+?\)', 'Critical PHP function call_user_func', '10'),
                              ('5', '\beval\b.*?(\(.+?\)|\{.+?\})', 'Critical function eval', '10'),
                              ('5', '\bexec\b.*?\(.+?\)', 'Critical function exec', '10'),
                              ('5', '\bmove_uploaded_file\b.*?\(.+?\)', 'Critical function move_uploaded_file', '11'),
                              ('5', '\bpassthru\b.*?\(.+?\)', 'Critical PHP function passthru', '8'),
                              ('5', '\bp(roc_)?open\b.*?\(.+?\)', 'Critical PHP function popen/proc_open', '10'),
                              ('5', 'shell_exec.*?\(.+?\)', 'critical PHP function shell_Exec', '10'),
                              ('5', 'system.*?\(.+?\)', 'Critical PHP function system', '10'),
                              ('5', '\bpreg_(replace|match)\b.*?\(.+?\)', 'Critical PHP function preg_match/preg_replace', '12'),
			      ('5', '\{\s*\$\s*\{.+?\}\s*\}', 'PHP complex curly syntax', '13'),
			      ('5', '\bexec\b.+?\bxp_cmdshell\b', 'MSSQL code execution xp_cmdshell', '10'),
       			      ('7', 'system\s\(', 'function system', '14'),
                              ('7', 'exec\(', 'command exec', '14'),
                              ('7', 'query\(', 'function query', '14'),
                              ('7', 'cmd', 'cmd', '14'),
                              ('3', 'setcookie\(.*\)', 'Initialize cookie', '15'),
                              ('3', 'session_set_cookie_params', 'parameters cookie', '15'),
                              ('6', '\.\.[\/\\]', 'Directory traversal', '16'),
			      ('6', '%(c0\.|af\.|5c\.)', 'Directory traversal unicode + urlencoding', '16'),
			      ('6', '%2e%2e[\/\\]', 'Directory traversal urlencoding', '16'),
                              ('6', '%c0%ae[\/\\]', 'Directory traversal unicode + urlencoding', '16')]

	connection= sqlite3.connect("Fraudatanalyzer.db")

	cursor= connection.cursor()

	cursor.execute("CREATE TABLE versions (version_id INTEGER PRIMARY KEY AUTOINCREMENT, version TEXT NOT NULL, expression TEXT NOT NULL, description TEXT NOT NULL)")
	cursor.execute("CREATE TABLE functions (function_id INTEGER PRIMARY KEY AUTOINCREMENT, function TEXT NOT NULL, expression TEXT NOT NULL, alternative TEXT NOT NULL, description TEXT NOT NULL, versionob INTEGER, FOREIGN KEY (versionob) REFERENCES versions(version_id))")
	cursor.execute("CREATE TABLE recommendations (recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT, liga TEXT NOT NULL, description TEXT)")
	cursor.execute("CREATE TABLE names_vul (name_vul_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT)")
	cursor.execute("CREATE TABLE vulnerabilities (vulnerability_id INTEGER PRIMARY KEY AUTOINCREMENT, name INTEGER, expression TEXT NOT NULL, description TEXT NOT NULL, recommendation INTEGER, FOREIGN KEY (recommendation) REFERENCES recommendations(recommendation_id), FOREIGN KEY (name) REFERENCES names_vul(name_vul_id))")
	cursor.execute("CREATE TABLE reports (report_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, date_hour DATETIME NOT NULL, version TEXT NOT NULL)")
	cursor.execute("CREATE TABLE reports_vul_func (re_vul_func_id INTEGER PRIMARY KEY AUTOINCREMENT, line TEXT NOT NULL,file TEXT NOT NULL, functionob INTEGER, report INTEGER, vulnerability INTEGER, FOREIGN KEY (functionob) REFERENCES functions (function_id), FOREIGN KEY (report) REFERENCES reports (report_id), FOREIGN KEY (vulnerability) REFERENCES vulnerabilities(vulnerability_id))")
	cursor.executemany('INSERT INTO versions(version, expression, description) VALUES (?,?,?)', data_version)
	cursor.executemany('INSERT INTO recommendations(liga, description) VALUES (?,?)', data_recommendation)
	cursor.executemany('INSERT INTO names_vul(name, description) VALUES (?,?)', data_name_vul)
	cursor.executemany('INSERT INTO vulnerabilities(name, expression, description, recommendation) VALUES (?,?,?,?)', data_vulnerability)
	cursor.executemany('INSERT INTO functions(function, expression, alternative, description, versionob) VALUES (?,?,?,?,?)', data_function)

	connection.commit()
	print "Fraudatanalyzer.db created successfully";

	cursor.close()
create_tables()
