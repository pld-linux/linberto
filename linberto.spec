Summary:	-
Summary(pl):	-
Name:		linberto
Version:	1.0.0
Release:	1
Group:		-
Group(pl):	-
Copyright:	GPL
Source0:	http://www.grigna.com/diego/linux/linberto/%{name}-%{version}.tar.gz
URL:		http://www.grigna.com/diego/linux/linberto/
BuildPrereq:	-
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
It is a jump around arcade game. Main features: nice graphics, music, sound
fx, english/spanish language support, runtime help and setup, built in level
editor and much more.

%description -l pl

%prep
%setup  -q

%build
(autoheader/autoconf/automake)
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info* \
	$RPM_BUILD_ROOT%{_mandir}/man*/* \
	README ChangeLog 

%pre

%preun

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%changelog
