# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	perl-script to send XMPP (jabber) messages
Summary(pl.UTF-8):	skrypt perlowy do wysyłania wiaomości XMPP (jabber)
Name:		sendxmpp
Version:	0.0.8
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://sendxmpp.platon.sk/%{name}-%{version}.tar.gz
# Source0-md5:	8a041f4940274f4d1e72e76fcc95e689
URL:		http://sendxmpp.platon.sk/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Net-XMPP
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sendxmpp is a perl-script to send XMPP (jabber) messages, similar to
what mail(1) does for mail.

%description -l pl.UTF-8
sendxmpp jest perlowym skryptem służącym do wysyłania wiadomości XMPP
(jabber), podobnie jak komenda mail(1) wysyła wiadomości pocztowe.

%prep
%setup -q

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
%doc Changes README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
