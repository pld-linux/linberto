Summary:	It is a jump around arcade game
Summary(pl):	Gra polegaj±ca na skakaniu
Name:		linberto
Version:	1.0.5
Release:	2
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	http://www.grigna.com/diego/linux/linberto/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-openscore.patch
URL:		http://www.grigna.com/diego/linux/linberto/
BuildRequires:	svgalib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a jump around arcade game. Main features: nice graphics, music,
sound fx, English/Spanish language support, runtime help and setup,
built in level editor and much more.

%description -l pl
To jest gra polegaj±ca na skakaniu. G³ówne zalety: przyjemna grafika,
muzyka, efekty d¼wiêkowe, wsparcie dla jêzyka angielskiego i
hiszpañskiego, dostêpna pomoc i konfiguracja, wbudowany edytor
poziomów... i wiele innych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} -C src CCOPTS="%{rpmcflags}" PREFIX=%{_prefix} \
	SCOREFILE=/var/games/linberto-scores.dat \
	CONFIGFILE=%{_sysconfdir}/linberto.conf \
	LIBDIR=%{_datadir}/linberto

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_mandir}/man6,/var/games,%{_sysconfdir}}

%{__make} -C src install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} \
	SCOREFILE=/var/games/linberto-scores.dat \
	CONFIGFILE=%{_sysconfdir}/linberto.conf \
	LIBDIR=%{_datadir}/linberto \
	INSMANDIR=%{_mandir}/man6 \
	INSMANDIRIT=%{_mandir}/it/man6 \
	INSMANDIRES=%{_mandir}/es/man6

touch $RPM_BUILD_ROOT/var/games/linberto-scores.dat
touch $RPM_BUILD_ROOT%{_sysconfdir}/linberto.conf

rm -f doc/{COPYING,INSTALL*,LSM*} doc/*/{COPYING,INST*}
gzip -9nf doc/*.txt doc/*/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*.gz
%lang(es) %doc doc/es
%lang(it) %doc doc/it
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/linberto
%{_mandir}/man6/*
%lang(es) %{_mandir}/es/man6/*
%lang(it) %{_mandir}/it/man6/*
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/linberto-scores.dat
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/linberto.conf
