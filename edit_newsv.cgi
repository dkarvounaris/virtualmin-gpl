#!/usr/local/bin/perl
# Show a form for changing global spam and virus scanning options

require './virtual-server-lib.pl';
&can_edit_templates() || &error($text{'sv_ecannot'});
&ui_print_header(undef, $text{'sv_title'}, "", "sv");

print "$text{'sv_desc'}<p>\n";
print &ui_form_start("save_newsv.cgi", "post");
print &ui_table_start($text{'sv_header'}, "width=100%", 2, [ "width=30%" ]);
@doms = &list_domains();

if ($config{'spam'}) {
	# Spam scanning program
	# XXX

	# Spamc host
	# XXX

	# Spamc max size
	# XXX
	}

# Virus scanning program
if ($config{'virus'}) {
	# Domain count
	@vdoms = grep { $_->{'virus'} } @doms;
	print &ui_table_row($text{'sv_vdoms'},
		scalar(@vdoms) || $text{'sv_none'});

	# Virus scanner
	$scanner = &get_global_virus_scanner();
	print &ui_table_row(&hlink($text{'spam_scanner'}, 'spam_scanner'),
		&ui_radio('scanner', $scanner eq 'clamscan' ? 0 :
				     $scanner eq 'clamdscan' ? 1 : 2,
		  [ [ 0, $text{'spam_scanner0'}."<br>" ],
		    [ 1, $text{'spam_scanner1'}."<br>" ],
		    [ 2, &text('spam_scanner2',
				&ui_textbox("scanprog", $scanner, 40)) ] ]));
	}

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'save'} ] ]);

&ui_print_footer("", $text{'index_return'});

