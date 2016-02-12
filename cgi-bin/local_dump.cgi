#!/usr/bin/perl
use warnings;
use strict;

my @lcommands = ("uptime", "df -h", "ping 8.8.8.8 -c 3", "uname -a", "date");

print "Content-type:text/html\r\n\r\n";
print <<END;
<html>
<head>
	<title>s1</title>
</head>
<body>
END

foreach (@lcommands)
{
	my $cmd_output = `$_`;
	$cmd_output =~ s/\n/<br \/>/g;
	print("\<b\>$_:\<\/b\>\<br \/>\r\n$cmd_output\<br\ \/>\r\n\<br\ \/>\r\n");
}

print <<END;
</body>
</html>
END



