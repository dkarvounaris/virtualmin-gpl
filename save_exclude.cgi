#!/usr/local/bin/perl
# Save per-domain excluded directories

require './virtual-server-lib.pl';
&ReadParse();
&error_setup($text{'exclude_err'});
$d = &get_domain($in{'dom'});
&can_edit_domain($d) || &error($text{'edit_ecannot'});
&can_edit_exclude() || &error($text{'exclude_ecannot'});

# Validate and save inputs
@exclude = grep { /\S/ } split(/\r?\n/, $in{'dirs'});
foreach $e (@exclude) {
	$e !~ /^\// || &error(&text('exclude_eabs', $e));
	$e !~ /\.\./ || &error(&text('exclude_edot', $e));
	}
&save_backup_excludes($d, \@exclude);

# All done
&webmin_log("exclude", "domain", $d->{'dom'});
&domain_redirect($d);
