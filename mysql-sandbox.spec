#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MySQL
%define		pnam	Sandbox
Summary:	Quickly installs MySQL side server, either standalone or in groups
Name:		mysql-sandbox
Version:	3.0.04
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MySQL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3670480412c0b381075322f765b19805
URL:		http://www.mysqlsandbox.net/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# matches 'use mysql' from inline text
%define		_noautoreq	'perl(mysql)'

%description
MySQL Sandbox is a tool that installs one or more MySQL servers within
seconds, easily, securely, and with full control.

Once installed, the sandbox is easily used and maintained, without
using complex options.

Replicated and multiple sandboxes can be used individually or all at
once.


%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/low_level_make_sandbox
%attr(755,root,root) %{_bindir}/make_multiple_custom_sandbox
%attr(755,root,root) %{_bindir}/make_multiple_sandbox
%attr(755,root,root) %{_bindir}/make_replication_sandbox
%attr(755,root,root) %{_bindir}/make_sandbox
%attr(755,root,root) %{_bindir}/make_sandbox_from_installed
%attr(755,root,root) %{_bindir}/make_sandbox_from_source
%attr(755,root,root) %{_bindir}/sandbox
%attr(755,root,root) %{_bindir}/sb
%attr(755,root,root) %{_bindir}/sbtool
%attr(755,root,root) %{_bindir}/test_sandbox
%{perl_vendorlib}/MySQL/*.pm
%{perl_vendorlib}/MySQL/Sandbox
%{_mandir}/man3/*
