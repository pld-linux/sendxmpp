# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"

Summary:	perl-script to send XMPP (jabber) messages
Summary(pl.UTF-8):	skrypt perlowy do wysyłania wiadomości XMPP (jabber)
Name:		sendxmpp
Version:	1.23
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	https://github.com/lhost/sendxmpp/archive/v1.23.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	c034aa7caf04a1769935c53fb25ba39f
URL:		http://sendxmpp.hostname.sk/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Net-XMPP
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sendxmpp is a Perl script to send XMPP (jabber) messages, similar to
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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/sendxmpp/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/sendxmpp
%{_mandir}/man1/sendxmpp.1*
