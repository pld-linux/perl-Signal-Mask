#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Signal
%define		pnam	Mask
Summary:	Signal::Mask - Signal masks made easy
Name:		perl-Signal-Mask
Version:	0.008
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Signal/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1cd1832d50e76931b69db3452e728c64
URL:		https://metacpan.org/release/Signal-Mask
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-IPC-Signal
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Signal::Mask is an abstraction around your process or thread signal
mask. It is used to fetch and/or change the signal mask of the calling
process or thread. The signal mask is the set of signals whose
delivery is currently blocked for the caller. It is available as the
global hash %Signal::Mask.

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
%doc Changes INSTALL README
%dir %{perl_vendorlib}/Signal
%{perl_vendorlib}/Signal/*.pm
%{_mandir}/man3/*
