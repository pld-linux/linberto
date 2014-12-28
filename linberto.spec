Summary:	It is a jump around arcade game
Summary(pl.UTF-8):	Gra polegająca na skakaniu
Name:		linberto
Version:	1.0.5
Release:	6
License:	GPL
Group:		Applications/Games
Source0:	http://www.grigna.com/diego/linux/linberto/%{name}-%{version}.tar.gz
# Source0-md5:	3ec925bb1c25043f302f51c7224bbb56
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-openscore.patch
URL:		http://www.grigna.com/diego/linux/linberto/
BuildRequires:	gettext-tools
BuildRequires:	svgalib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a jump around arcade game. Main features: nice graphics, music,
sound fx, English/Spanish language support, runtime help and setup,
built in level editor and much more.

%description -l pl.UTF-8
To jest gra polegająca na skakaniu. Główne zalety: przyjemna grafika,
muzyka, efekty dźwiękowe, wsparcie dla języka angielskiego i
hiszpańskiego, dostępna pomoc i konfiguracja, wbudowany edytor
poziomów... i wiele innych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} -C src \
	CCOPTS="%{rpmcflags}" \
	PREFIX=%{_prefix} \
	SCOREFILE=/var/games/linberto-scores.dat \
	CONFIGFILE=%{_sysconfdir}/linberto.conf \
	LIBDIR=%{_datadir}/linberto

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_mandir}/man6,/var/games,%{_sysconfdir}}

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	SCOREFILE=/var/games/linberto-scores.dat \
	CONFIGFILE=%{_sysconfdir}/linberto.conf \
	LIBDIR=%{_datadir}/linberto \
	INSMANDIR=%{_mandir}/man6 \
	INSMANDIRIT=%{_mandir}/it/man6 \
	INSMANDIRES=%{_mandir}/es/man6

touch $RPM_BUILD_ROOT/var/games/linberto-scores.dat
touch $RPM_BUILD_ROOT%{_sysconfdir}/linberto.conf

rm -f doc/{COPYING,INSTALL*,LSM*} doc/*/{COPYING,INST*}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*
%lang(es) %doc doc/es
%lang(it) %doc doc/it
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/linberto
%{_mandir}/man6/*
%lang(es) %{_mandir}/es/man6/*
%lang(it) %{_mandir}/it/man6/*
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/linberto-scores.dat
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/linberto.conf
