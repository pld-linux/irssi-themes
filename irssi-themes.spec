Summary:	Irssi themes pack
Name:		irssi-themes
%define	_snap 20051016
Version:	0.%{_snap}
Release:	0.2
License:	freeware
Group:		Applications/Communications
URL:		http://www.irssi.org/?page=themes
Requires:	irssi
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	559fce778a24fb3955524edae639d1a9
Source1:	%{name}-generate.sh
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themedir	%{_datadir}/irssi/themes

%description
Irssi themes pack.

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
