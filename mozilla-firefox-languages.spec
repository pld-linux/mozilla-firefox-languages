# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=%{version}
U=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Firefox
Summary(pl.UTF-8):	Pakiety językowe dla Firefoksa
Name:		mozilla-firefox-languages
Version:	34.0.5
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	0115143500dd545f20887fff6a005a4b
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	d2f93adc6cfe34d04bd7dcc17d457317
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	baf1f70c865462ab1d75e5ff55fde09b
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source3-md5:	43b7fbdb60d2cb3b25adc227fcfc0b62
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source4-md5:	1c466a5e9f62ba0ba440e20dcb70d4d7
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source5-md5:	e577b2421f436e230a0cf1c113c39df1
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source6-md5:	31128db58f73e912847e37aea840c9c4
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source7-md5:	eb3c55d17c984e8a6433f0136249c87e
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source8-md5:	0209518ebeea0d340e324bf15393c366
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source9-md5:	d594a02075df66f20a8bf71875fb4897
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source10-md5:	f77c19aad70708cc387a7d23c9f9b5c6
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source11-md5:	9503098e2bf4169cb09a0bc87c3f1cb6
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source12-md5:	f71f651b35f8939b9b1519fbe74b14b0
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source13-md5:	fb0c268ad086f0ae66c18513673e1a6f
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	4c8b5a1dfc3e2ec59a7ff7da8c769182
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/csb.xpi
# Source15-md5:	b2abe8aa6b8c07662e8599b5319d89a8
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source16-md5:	49325c5c211a70de621fb1ea6334ad4b
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source17-md5:	1baf52fd7156c78f56a88d2c6292fa1a
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source18-md5:	89090bbcab8bd98e5aab29c38ee19fec
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source19-md5:	4b0220fc777307cee60434e0921e4681
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source20-md5:	261e8b37552037e3965bce8b72574dc9
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source21-md5:	a54b73efab1fd4d7383524ac34ea7e6d
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source22-md5:	cb54aeb496b852f8ec65419011e377b7
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source23-md5:	de2be00327e212156083270b09109f57
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source24-md5:	0acbd440022891461e056121ae6329d5
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source25-md5:	037d9e4b93d12ce3d8fe4a411fc1b33e
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source26-md5:	bf361c7951cb289bf7a4eb7d6e249acc
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source27-md5:	fb83cd37336aabedfc756688197770ff
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source28-md5:	3e036cafe87acdf5faed11858899073d
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source29-md5:	e7e1e90153d0bd0773aaaa32d330e5d8
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source30-md5:	176942676510838ff942da2e0a178555
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source31-md5:	c9acea79e62ec1c0a913ec18cd3376dd
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source32-md5:	e934c89fab1c263e6682759e199101d5
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source33-md5:	6a9cd0ebbed11c6e3439e79a5fb61232
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source34-md5:	e651aba280d298ef68b9a19456166e34
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source35-md5:	5be6fbea664c792be0a8b5e69242f6e3
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source36-md5:	2dc4c39ca4058867602478ef61c21487
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source37-md5:	3659fd32aae70259f1490b4b77ef73a5
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source38-md5:	d4121e8a7ed003a61ac835f6a7c7a9c6
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source39-md5:	e8da734046f68b0fcc36a7382fb16171
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source40-md5:	537d8d114d4e07d714e5a1bf47b2ae3c
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source41-md5:	0f308d89fbb56b74d1c277c0b0d637be
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source42-md5:	407f368126dc3b58f44656d2c0d333e0
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source43-md5:	cf50a4d49323a8c8afef4dff4b54cb53
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source44-md5:	543f5606082008b1ddeb0e4a4c541d5c
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source45-md5:	8142659e1c39224429e06deaed8d96a8
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source46-md5:	a3b1c993ce2552d315d4eac3e7ae31a6
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source47-md5:	33ffddadb5c66c983cbd00622b523d63
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source48-md5:	6b2b27cebbe4514c58d556548a6af75b
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source49-md5:	435218c709bc7e0fe6ca203d70603c32
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source50-md5:	f8969cc6abcecc6ae4bd3f2b72db0b18
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source51-md5:	b4feec05dc05f5a06731b2a981a099ce
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source52-md5:	6463b045558ee19f512a4f575185e72a
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source53-md5:	ffa1a181abd3f6a7169c8909de2a0166
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source54-md5:	c06f4a9c383ca2ecb560eb9a4f4bba18
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source55-md5:	de40d45a0ed5dc0e0b5c5202aeac8bf5
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source56-md5:	e026d1a2eddc8c964f9c6e03d6cd1d37
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source57-md5:	aa8cfe86c7e8606260a101398f5c454c
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source58-md5:	2c97b7681caa526972a787d257dc3b67
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source59-md5:	ac4b02de391ce4f32e33cc2203939599
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source60-md5:	fe2a25edabb8c1a5a0fdce44ae5a8d43
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source61-md5:	f33b165de98b96034764d964d6e7d8e5
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source62-md5:	8dea7a63caa2a6b0fea1271af9c30561
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source63-md5:	f6718e7714b8340cbf14f5e93e53594f
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source64-md5:	c5a9ca7dbac79f35c2ebe4e2e1bfb49f
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source65-md5:	b052f82e39fff33bb175236ce27834bd
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source66-md5:	643dd03e0875c694c658afa33ae25d8a
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source67-md5:	0afb28541359a00b1a7c632332475903
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source68-md5:	67d23a123be9007f31722186c74bab85
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source69-md5:	1ccc34760b50c26b710604a2657b8692
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source70-md5:	208ef966a36644f850f7f02ca3755d03
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source71-md5:	2d570f73653c6ecf2a9fafd1b89f7ce7
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source72-md5:	b4fe52b92c2e637e34e97d0898cdfe4e
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source73-md5:	fd9f18a1330b053490f5ad9b355856f5
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source74-md5:	7e25946274a66fcb4c8520369643c7bb
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source75-md5:	8ee97120e9787b3e8b0ed1815b9a3f47
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source76-md5:	47986cd25e6ed4c97778ec7a4e659357
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source77-md5:	fe07b8067f2b5c5d1af16cae98c82647
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source78-md5:	90b1eb1cc6be85820b9b847330de4fad
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source79-md5:	f9cfa9ddcd8ea555aeb32560e17579ba
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source80-md5:	a0b084c931d956aa5e3227bf2f3ca415
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source81-md5:	12bc76d2ccd9248c362a7312c6d512c9
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source82-md5:	a3611c4f3e939476aaeee5de13385ee4
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source83-md5:	947147e6de943a217514ce986e970e56
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source84-md5:	6e5982a50cf018e60d1bd53a061894c0
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source85-md5:	41a8986f629e423c92c53a415da754f1
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source86-md5:	3b70320e99cc352a217dc5a508bb37ad
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source87-md5:	419e0bb94eb52d6e4828cf7df1c64dde
Source88:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source88-md5:	26f2008991c6620231811314c564c69e
URL:		http://www.mozilla.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		firefoxdir	%{_datadir}/mozilla-firefox

%description
Language packs for Firefox.

%description -l pl.UTF-8
Pakiety językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ach
Summary:	Acoli resources for Firefox
Summary(pl.UTF-8):	Pliki językowe aczoli dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ach
Acoli resources for Firefox.

%description -n mozilla-firefox-lang-ach -l pl.UTF-8
Pliki językowe aczoli dla Firefoksa.

%package -n mozilla-firefox-lang-af
Summary:	Afrikaans resources for Firefox
Summary(pl.UTF-8):	Afrykanerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-af
Afrikaans resources for Firefox.

%description -n mozilla-firefox-lang-af -l pl.UTF-8
Afrykanerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-an
Summary:	Aragonese resources for Firefox
Summary(pl.UTF-8):	Aragońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-an
Aragonese resources for Firefox.

%description -n mozilla-firefox-lang-an -l pl.UTF-8
Aragońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ar
Summary:	Arabic resources for Firefox
Summary(pl.UTF-8):	Arabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ar
Arabic resources for Firefox.

%description -n mozilla-firefox-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-as
Summary:	Assamese resources for Firefox
Summary(pl.UTF-8):	Asamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}

%description -n mozilla-firefox-lang-as
Assamese resources for Firefox.

%description -n mozilla-firefox-lang-as -l pl.UTF-8
Asamskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ast
Summary:	Asturian resources for Firefox
Summary(pl.UTF-8):	Asturyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ast
Asturian resources for Firefox.

%description -n mozilla-firefox-lang-ast -l pl.UTF-8
Asturyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-az
Summary:	Azerbaijani resources for Firefox
Summary(pl.UTF-8):	Azerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-az
Azerbaijani resources for Firefox.

%description -n mozilla-firefox-lang-az -l pl.UTF-8
Azerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-be
Summary:	Belarusian resources for Firefox
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-be
Belarusian resources for Firefox.

%description -n mozilla-firefox-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bg
Summary:	Bulgarian resources for Firefox
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bg
Bulgarian resources for Firefox.

%description -n mozilla-firefox-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bn
Summary:	Bengali (Bangladesh) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bn
Bengali (Bangladesh) resources for Firefox.

%description -n mozilla-firefox-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu).

%package -n mozilla-firefox-lang-bn_IN
Summary:	Bengali (India) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bn_IN
Bengali (India) resources for Firefox.

%description -n mozilla-firefox-lang-bn_IN -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n mozilla-firefox-lang-br
Summary:	Breton resources for Firefox
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-br
Breton resources for Firefox.

%description -n mozilla-firefox-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bs
Summary:	Bosnian resources for Firefox
Summary(pl.UTF-8):	Bośniackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bs
Bosnian resources for Firefox.

%description -n mozilla-firefox-lang-bs -l pl.UTF-8
Bośniackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ca
Summary:	Catalan resources for Firefox
Summary(ca.UTF-8):	Recursos catalans per Firefox
Summary(es.UTF-8):	Recursos catalanes para Firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.softcatala.org/projectes/mozilla/
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ca
Catalan resources for Firefox.

%description -n mozilla-firefox-lang-ca -l ca.UTF-8
Recursos catalans per Firefox.

%description -n mozilla-firefox-lang-ca -l es.UTF-8
Recursos catalanes para Firefox.

%description -n mozilla-firefox-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-cs
Summary:	Czech resources for Firefox
Summary(pl.UTF-8):	Czeskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-cs
Czech resources for Firefox.

%description -n mozilla-firefox-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-csb
Summary:	Kashubian resources for Firefox
Summary(pl.UTF-8):	Kaszubskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-csb
Kashubian resources for Firefox.

%description -n mozilla-firefox-lang-csb -l pl.UTF-8
Kaszubskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-cy
Summary:	Welsh resources for Firefox
Summary(pl.UTF-8):	Walijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-cy
Welsh resources for Firefox.

%description -n mozilla-firefox-lang-cy -l pl.UTF-8
Walijskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-da
Summary:	Danish resources for Firefox
Summary(pl.UTF-8):	Duńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-da
Danish resources for Firefox.

%description -n mozilla-firefox-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-de
Summary:	German resources for Firefox
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-de
German resources for Firefox.

%description -n mozilla-firefox-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-dsb
Summary:	Lower Sorbian resources for Firefox
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-dsb
Lower Sorbian resources for Firefox.

%description -n mozilla-firefox-lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-el
Summary:	Greek resources for Firefox
Summary(pl.UTF-8):	Greckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-el
Greek resources for Firefox.

%description -n mozilla-firefox-lang-el -l pl.UTF-8
Greckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_GB
Summary:	English (British) resources for Firefox
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_GB
English (British) resources for Firefox.

%description -n mozilla-firefox-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_US
Summary:	English (American) resources for Firefox
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_US
English (American) resources for Firefox.

%description -n mozilla-firefox-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_ZA
Summary:	English (South Africa) resources for Firefox
Summary(pl.UTF-8):	Angielskie pliki językowe dla Firefoksa (wersja dla RPA)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_ZA
English (South Africa) resources for Firefox.

%description -n mozilla-firefox-lang-en_ZA -l pl.UTF-8
Angielskie pliki językowe dla Firefoksa (wersja dla Republiki
Południowej Afryki).

%package -n mozilla-firefox-lang-eo
Summary:	Esperanto resources for Firefox
Summary(pl.UTF-8):	Pliki językowe esperanto dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-eo
Esperanto resources for Firefox.

%description -n mozilla-firefox-lang-eo -l pl.UTF-8
Pliki językowe esperanto dla Firefoksa.

%package -n mozilla-firefox-lang-es_AR
Summary:	Spanish (Andorra) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per Firefox
Summary(es.UTF-8):	Recursos españoles (Andorra) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_AR
Spanish (Spain) resources for Firefox.

%description -n mozilla-firefox-lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per Firefox.

%description -n mozilla-firefox-lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para Firefox.

%description -n mozilla-firefox-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory).

%package -n mozilla-firefox-lang-es_CL
Summary:	Spanish (Chile) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Xile) per Firefox
Summary(es.UTF-8):	Recursos españoles (Chile) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_CL
Spanish (Chile) resources for Firefox.

%description -n mozilla-firefox-lang-es_CL -l ca.UTF-8
Recursos espanyols (Xile) per Firefox.

%description -n mozilla-firefox-lang-es_CL -l es.UTF-8
Recursos españoles (Chile) para Firefox.

%description -n mozilla-firefox-lang-es_CL -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile).

%package -n mozilla-firefox-lang-es
Summary:	Spanish (Spain) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per Firefox
Summary(es.UTF-8):	Recursos españoles (España) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es
Spanish (Spain) resources for Firefox.

%description -n mozilla-firefox-lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per Firefox.

%description -n mozilla-firefox-lang-es -l es.UTF-8
Recursos españoles (España) para Firefox.

%description -n mozilla-firefox-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii).

%package -n mozilla-firefox-lang-es_MX
Summary:	Spanish (Mexico) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Mèxic) per Firefox
Summary(es.UTF-8):	Recursos españoles (México) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_MX
Spanish (Mexico) resources for Firefox.

%description -n mozilla-firefox-lang-es_MX -l ca.UTF-8
Recursos espanyols (Mèxic) per Firefox.

%description -n mozilla-firefox-lang-es_MX -l es.UTF-8
Recursos españoles (México) para Firefox.

%description -n mozilla-firefox-lang-es_MX -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku).

%package -n mozilla-firefox-lang-et
Summary:	Estonian resources for Firefox
Summary(pl.UTF-8):	Estońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-et
Estonian resources for Firefox.

%description -n mozilla-firefox-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-eu
Summary:	Basque resources for Firefox
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-eu
Basque resources for Firefox.

%description -n mozilla-firefox-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fa
Summary:	Persian resources for Firefox
Summary(pl.UTF-8):	Perskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fa
Persian resources for Firefox.

%description -n mozilla-firefox-lang-fa -l pl.UTF-8
Perskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ff
Summary:	Fulah resources for Firefox
Summary(pl.UTF-8):	Pliki językowe fulani dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ff
Fulah resources for Firefox.

%description -n mozilla-firefox-lang-ff -l pl.UTF-8
Pliki językowe fulani dla Firefoksa.

%package -n mozilla-firefox-lang-fi
Summary:	Finnish resources for Firefox
Summary(pl.UTF-8):	Fińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fi
Finnish resources for Firefox.

%description -n mozilla-firefox-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fr
Summary:	French resources for Firefox
Summary(pl.UTF-8):	Francuskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fr
French resources for Firefox.

%description -n mozilla-firefox-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fy
Summary:	Frisian resources for Firefox
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fy
Frisian resources for Firefox.

%description -n mozilla-firefox-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ga
Summary:	Irish resources for Firefox
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ga
Irish resources for Firefox.

%description -n mozilla-firefox-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gd
Summary:	Gaelic resources for Firefox
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gd
Gaelic resources for Firefox.

%description -n mozilla-firefox-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gl
Summary:	Galician resources for Firefox
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gl
Galician resources for Firefox.

%description -n mozilla-firefox-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gu
Summary:	Gujarati resources for Firefox
Summary(pl.UTF-8):	Pliki językowe gudźarati dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gu
Gujarati resources for Firefox.

%description -n mozilla-firefox-lang-gu -l pl.UTF-8
Pliki językowe gudźarati dla Firefoksa.

%package -n mozilla-firefox-lang-he
Summary:	Hebrew resources for Firefox
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-he
Hebrew resources for Firefox.

%description -n mozilla-firefox-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hi
Summary:	Hindi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe hindi dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hi
Hindi resources for Firefox.

%description -n mozilla-firefox-lang-hi -l pl.UTF-8
Pliki językowe hindi dla Firefoksa.

%package -n mozilla-firefox-lang-hr
Summary:	Croatian resources for Firefox
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hr
Croatian resources for Firefox.

%description -n mozilla-firefox-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hsb
Summary:	Upper Sorbian resources for Firefox
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hsb
Upper Sorbian resources for Firefox.

%description -n mozilla-firefox-lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hu
Summary:	Hungarian resources for Firefox
Summary(hu.UTF-8):	Magyar nyelv Firefox-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hu
Hungarian resources for Firefox.

%description -n mozilla-firefox-lang-hu -l hu.UTF-8
Magyar nyelv Firefox-hez.

%description -n mozilla-firefox-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hy
Summary:	Armenian resources for Firefox
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hy
Armenian resources for Firefox.

%description -n mozilla-firefox-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-id
Summary:	Indonesian resources for Firefox
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-id
Indonesian resources for Firefox.

%description -n mozilla-firefox-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-is
Summary:	Icelandic resources for Firefox
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-is
Icelandic resources for Firefox.

%description -n mozilla-firefox-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-it
Summary:	Italian resources for Firefox
Summary(pl.UTF-8):	Włoskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-it
Italian resources for Firefox.

%description -n mozilla-firefox-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ja
Summary:	Japanese resources for Firefox
Summary(pl.UTF-8):	Japońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ja
Japanese resources for Firefox.

%description -n mozilla-firefox-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-kk
Summary:	Kazakh resources for Firefox
Summary(pl.UTF-8):	Kazachskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-kk
Kazakh resources for Firefox.

%description -n mozilla-firefox-lang-kk -l pl.UTF-8
Kazachskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-km
Summary:	Khmer resources for Firefox
Summary(pl.UTF-8):	Khmerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-km
Khmer resources for Firefox.

%description -n mozilla-firefox-lang-km -l pl.UTF-8
Khmerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-kn
Summary:	Kannada resources for Firefox
Summary(pl.UTF-8):	Pliki językowe kannada dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-kn
Kannada resources for Firefox.

%description -n mozilla-firefox-lang-kn -l pl.UTF-8
Pliki językowe kannada dla Firefoksa.

%package -n mozilla-firefox-lang-ko
Summary:	Korean resources for Firefox
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ko
Korean resources for Firefox.

%description -n mozilla-firefox-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ku
Summary:	Kurdish resources for Firefox
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ku
Kurdish resources for Firefox.

%description -n mozilla-firefox-lang-ku -l pl.UTF-8
Kurdyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lij
Summary:	Ligurian resources for Firefox
Summary(pl.UTF-8):	Liguryjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lij
Ligurian resources for Firefox.

%description -n mozilla-firefox-lang-lij -l pl.UTF-8
Liguryjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lt
Summary:	Lithuanian resources for Firefox
Summary(pl.UTF-8):	Litewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lt
Lithuanian resources for Firefox.

%description -n mozilla-firefox-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lv
Summary:	Latvian resources for Firefox
Summary(pl.UTF-8):	Łotewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lv
Latvian resources for Firefox.

%description -n mozilla-firefox-lang-lv -l pl.UTF-8
Łotewskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-mai
Summary:	Maithili resources for Firefox
Summary(pl.UTF-8):	Pliki językowe maithili dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mai
Maithili resources for Firefox.

%description -n mozilla-firefox-lang-mai -l pl.UTF-8
Pliki językowe maithili dla Firefoksa.

%package -n mozilla-firefox-lang-mk
Summary:	Macedonian resources for Firefox
Summary(pl.UTF-8):	Macedońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mk
Macedonian resources for Firefox.

%description -n mozilla-firefox-lang-mk -l pl.UTF-8
Macedońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ml
Summary:	Malayalam resources for Firefox
Summary(pl.UTF-8):	Pliki językowe malajalam dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ml
Malayalam resources for Firefox.

%description -n mozilla-firefox-lang-ml -l pl.UTF-8
Pliki językowe malajalam dla Firefoksa.

%package -n mozilla-firefox-lang-mr
Summary:	Marathi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe marathi dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mr
Marathi resources for Firefox.

%description -n mozilla-firefox-lang-mr -l pl.UTF-8
Pliki językowe marathi dla Firefoksa.

%package -n mozilla-firefox-lang-ms
Summary:	Malay resources for Firefox
Summary(pl.UTF-8):	Malajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ms
Malay resources for Firefox.

%description -n mozilla-firefox-lang-ms -l pl.UTF-8
Malajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nb
Summary:	Norwegian Bokmaal resources for Firefox
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nb
Norwegian Bokmaal resources for Firefox.

%description -n mozilla-firefox-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nl
Summary:	Dutch resources for Firefox
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nl
Dutch resources for Firefox.

%description -n mozilla-firefox-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nn
Summary:	Norwegian Nynorsk resources for Firefox
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nn
Norwegian Nynorsk resources for Firefox.

%description -n mozilla-firefox-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-or
Summary:	Oriya resources for Firefox
Summary(pl.UTF-8):	Pliki językowe orija dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-or
Oriya resources for Firefox.

%description -n mozilla-firefox-lang-or -l pl.UTF-8
Pliki językowe orija dla Firefoksa.

%package -n mozilla-firefox-lang-pa
Summary:	Panjabi resources for Firefox
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pa
Panjabi resources for Firefox.

%description -n mozilla-firefox-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pl
Summary:	Polish resources for Firefox
Summary(pl.UTF-8):	Polskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.firefox.pl/
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pl
Polish resources for Firefox.

%description -n mozilla-firefox-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Firefox
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pt_BR
Portuguese (Brazil) resources for Firefox.

%description -n mozilla-firefox-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pt
Summary:	Portuguese (Portugal) resources for Firefox
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pt
Portuguese (Portugal) resources for Firefox.

%description -n mozilla-firefox-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii).

%package -n mozilla-firefox-lang-rm
Summary:	Romansh resources for Firefox
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-rm
Romansh resources for Firefox.

%description -n mozilla-firefox-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ro
Summary:	Romanian resources for Firefox
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ro
Romanian resources for Firefox.

%description -n mozilla-firefox-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ru
Summary:	Russian resources for Firefox
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ru
Russian resources for Firefox.

%description -n mozilla-firefox-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-si
Summary:	Sinhala resources for Firefox
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-si
Sinhala resources for Firefox.

%description -n mozilla-firefox-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sk
Summary:	Slovak resources for Firefox
Summary(pl.UTF-8):	Słowackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sk
Slovak resources for Firefox.

%description -n mozilla-firefox-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sl
Summary:	Slovene resources for Firefox
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sl
Slovene resources for Firefox.

%description -n mozilla-firefox-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-son
Summary:	Songhai resources for Firefox
Summary(pl.UTF-8):	Songhajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-son
Songhai resources for Firefox.

%description -n mozilla-firefox-lang-son -l pl.UTF-8
Songhajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sq
Summary:	Albanian resources for Firefox
Summary(pl.UTF-8):	Albańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sq
Albanian resources for Firefox.

%description -n mozilla-firefox-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sr
Summary:	Serbian resources for Firefox
Summary(pl.UTF-8):	Serbskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sr
Serbian resources for Firefox.

%description -n mozilla-firefox-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sv
Summary:	Swedish resources for Firefox
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sv
Swedish resources for Firefox.

%description -n mozilla-firefox-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ta
Summary:	Tamil (India) resources for Firefox
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ta
Tamil (India) resources for Firefox.

%description -n mozilla-firefox-lang-ta -l pl.UTF-8
Tamilskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n mozilla-firefox-lang-te
Summary:	Telugu resources for Firefox
Summary(pl.UTF-8):	Pliki językowe telugu dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-te
Telugu resources for Firefox.

%description -n mozilla-firefox-lang-te -l pl.UTF-8
Pliki językowe telugu dla Firefoksa.

%package -n mozilla-firefox-lang-th
Summary:	Thai resources for Firefox
Summary(pl.UTF-8):	Tajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-th
Thai resources for Firefox.

%description -n mozilla-firefox-lang-th -l pl.UTF-8
Tajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-tr
Summary:	Turkish resources for Firefox
Summary(pl.UTF-8):	Tureckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-tr
Turkish resources for Firefox.

%description -n mozilla-firefox-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-uk
Summary:	Ukrainian resources for Firefox
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-uk
Ukrainian resources for Firefox.

%description -n mozilla-firefox-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-vi
Summary:	Vietmanese resources for Firefox
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-vi
Vietmanese resources for Firefox.

%description -n mozilla-firefox-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-xh
Summary:	Xhosa resources for Firefox
Summary(pl.UTF-8):	Pliki językowe xhosa dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-xh
Xhosa resources for Firefox.

%description -n mozilla-firefox-lang-xh -l pl.UTF-8
Pliki językowe xhosa dla Firefoksa.

%package -n mozilla-firefox-lang-zh_CN
Summary:	Simplified Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zh_CN
Simplified Chinese resources for Firefox.

%description -n mozilla-firefox-lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-zh_TW
Summary:	Traditional Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zh_TW
Traditional Chinese resources for Firefox.

%description -n mozilla-firefox-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-zu
Summary:	Zulu resources for Firefox
Summary(pl.UTF-8):	Zuluskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zu
Zulu resources for Firefox.

%description -n mozilla-firefox-lang-zu -l pl.UTF-8
Zuluskie pliki językowe dla Firefoksa.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	install -d $lang
	cd $lang
	cp -p $file .
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 88 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{firefoxdir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{firefoxdir}/extensions/langpack-$basename@firefox.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n mozilla-firefox-lang-ach
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ach@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-af
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-af@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-an
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-an@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ar
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ar@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-as
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-as@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ast
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ast@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-az
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-az@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-be
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-be@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bg
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bg@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bn-BD@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bn_IN
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bn-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-br
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-br@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bs
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bs@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ca
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ca@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-cs
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-cs@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-csb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-csb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-cy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-cy@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-da
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-da@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-de
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-de@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-dsb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-dsb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-el
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-el@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_GB
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-GB@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_US
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-US@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_ZA
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-ZA@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-eo
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-eo@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_AR
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-AR@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_CL
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-CL@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-ES@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_MX
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-MX@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-et
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-et@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-eu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-eu@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fa
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fa@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ff
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ff@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fi@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fy-NL@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ga
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ga-IE@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gd
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gd@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gu-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-he
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-he@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hi-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hsb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hsb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hu@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hy-AM@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-id
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-id@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-is
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-is@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-it
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-it@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ja
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ja@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-kk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-kk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-km
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-km@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-kn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-kn@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ko
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ko@firefox.mozilla.org.xpi

#%files -n mozilla-firefox-lang-ku
#%defattr(644,root,root,755)
#%{firefoxdir}/extensions/langpack-ku@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lij
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lij@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lt
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lt@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lv
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lv@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mai
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mai@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ml
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ml@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ms
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ms@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nb-NO@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nn-NO@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-or
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-or@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pa
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pa-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pt_BR
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pt-BR@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pt
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pt-PT@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-rm
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-rm@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ro
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ro@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ru
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ru@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-si
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-si@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-son
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-son@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sq
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sq@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sv
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sv-SE@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ta
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ta@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-te
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-te@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-th
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-th@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-tr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-tr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-uk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-uk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-vi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-vi@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-xh
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-xh@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zh_CN
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zh-CN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zh_TW
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zh-TW@firefox.mozilla.org.xpi

#%files -n mozilla-firefox-lang-zu
#%defattr(644,root,root,755)
#%{firefoxdir}/extensions/langpack-zu@firefox.mozilla.org.xpi
