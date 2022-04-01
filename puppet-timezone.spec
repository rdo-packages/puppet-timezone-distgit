%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-timezone
%global commit 6f1a8e1af9e5a77a54df19d8426c4b408d69c41d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-timezone
Version:        6.1.0
Release:        3%{?alphatag}%{?dist}
Summary:        Manage timezone settings via Puppet.
License:        ASL 2.0

URL:            https://github.com/saz/puppet-timezone

Source0:        https://github.com/saz/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Manage timezone settings via Puppet.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/timezone/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/timezone/



%files
%{_datadir}/openstack-puppet/modules/timezone/


%changelog
* Fri Apr 01 2022 RDO <dev@lists.rdoproject.org> 6.1.0-3.6f1a8e1git
- Update to post 6.1.0 (6f1a8e1af9e5a77a54df19d8426c4b408d69c41d)



