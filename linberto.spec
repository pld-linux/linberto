Summary:	It is a jump around arcade game.
Name:		linberto
Version:	1.0.2
Release:	1
Group:		Games
Copyright:	GPL
Source:		http://www.grigna.com/diego/linux/linberto/%{name}-%{version}.tar.gz
Patch:		linberto-DESTDIR.patch
URL:		http://www.grigna.com/diego/linux/linberto/
BuildRequires:	svgalib-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
It is a jump around arcade game. Main features: nice graphics, music, sound
fx, english/spanish language support, runtime help and setup, built in level
editor and much more.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
make -C src CCOPTS="$RPM_OPT_FLAGS" prefix=%{_prefix} \
	SCOREFILE=/var/state/games/linberto-scores.dat \
	CONFIGFILE=/etc/linberto.conf \
	libdir=%{_datadir}/linberto \
	mandir=%{_mandir}/man6


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_mandir}/man6,/var/state/games,/etc}

make -C src install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} \
	SCOREFILE=/var/state/games/linberto-scores.dat \
	CONFIGFILE=/etc/linberto.conf \
	libdir=%{_datadir}/linberto \
	mandir=%{_mandir}/man6

touch $RPM_BUILD_ROOT/var/state/games/linberto-scores.dat
touch $RPM_BUILD_ROOT/etc/linberto.conf

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man6/* doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt.gz
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/linberto
%{_mandir}/man6/*
%attr(664,root,games) /var/state/games/linberto-scores.dat
%attr(664,root,games) %config /etc/linberto.conf
