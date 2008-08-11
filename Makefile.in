prefix=/usr
INSTALL=/usr/bin/install
BINDIR=$(prefix)/bin
MANDIR=$(prefix)/man/man1

none: 

man:
	pod2man jdresolve > jdresolve.1
	cat jdresolve.1 | gzip - > jdresolve.1.gz
	cat rhost.1 | gzip - > rhost.1.gz
	for FILE in AUTHORS README BUGS CHANGELOG CREDITS INSTALL TODO; do lynx --dump "$$FILE.html" | perl -ne "! /^Looking/ and print" > "$$FILE"; done

install:
	$(INSTALL) -m 755 -o bin -g bin jdresolve $(DESTDIR)$(BINDIR)
	$(INSTALL) -m 755 -o bin -g bin rhost $(DESTDIR)$(BINDIR)

	mkdir -p $(DESTDIR)$(MANDIR)
	$(INSTALL) -m 644 -o bin -g bin jdresolve.1 $(DESTDIR)$(MANDIR)
	$(INSTALL) -m 644 -o bin -g bin rhost.1 $(DESTDIR)$(MANDIR)

uninstall:
	rm $(DESTDIR)$(BINDIR)/jdresolve
	rm $(DESTDIR)$(BINDIR)/rhost

	rm $(DESTDIR)$(MANDIR)/jdresolve.1
	rm $(DESTDIR)$(MANDIR)/rhost.1

