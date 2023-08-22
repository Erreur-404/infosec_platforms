#!/bin/perl

my $filename = "|cat /etc/passwd|";
open(my $FILE, $filename) or die("file not found");
while (<$FILE>) {
    print "$filename: $_";
};
