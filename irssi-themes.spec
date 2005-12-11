Summary:	Irssi themes pack
Summary(pl):	Pakiet motywów dla Irssi
Name:		irssi-themes
%define	_snap 20051016
Version:	0.%{_snap}
Release:	1
License:	freeware
Group:		Applications/Communications
URL:		http://www.irssi.org/themes
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	559fce778a24fb3955524edae639d1a9
Source1:	%{name}-generate.sh
Requires:	irssi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themedir	%{_datadir}/irssi/themes

%description
Irssi themes pack.

%description -l pl
Pakiet motywów dla Irssi.

%prep
%setup -q -n %{name}-%{_snap}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themedir}
install *.theme $RPM_BUILD_ROOT%{_themedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themedir}/*
