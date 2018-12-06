# https://github.com/pkg/xattr
%global goipath github.com/pkg/xattr
Version:        0.3.1

%gometa -i

Name:           %{goname}
Release:        1%{?dist}
Summary:        Extended attribute support library for Go
License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz


%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/sys/unix)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q


%install
%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Sun Oct 14 2018 Steve Miller (copart) <code@rellims.com> - 0.3.1-1
- Bumped upstream version, bug fix release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Steve Miller (copart) <code@rellims.com> - 0.3.0-1
- First package for Fedora
