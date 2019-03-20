%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-timezone
%global commit e44be603765a247369504182b0c3af045d56f6f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-timezone
Version:        5.1.1
Release:        1%{?alphatag}%{?dist}
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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 5.1.1-1.e44be60git
- Update to post 5.1.1 (e44be603765a247369504182b0c3af045d56f6f1)



