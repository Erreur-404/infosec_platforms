#!/bin/perl

use DBI;

$user = "user1";
$password = "hello";

my $dbh = DBI->connect("DBI:MariaDB:test1", $user, $password) or die "Could not connect to database";

if (defined $ARGV[0]) {
    print $dbh->quote($ARGV[0]);
}
else {
    print "Usage : ./quoted_input_visualizer.pl <input>";
}
print "\n";
