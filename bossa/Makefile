#
# Copyright (C) 2006-2012 OpenWrt.org
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=bossa
PKG_VERSION:=1.6.1-arduino
PKG_RELEASE:=$(PKG_SOURCE_VERSION)

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/shumatech/BOSSA.git
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE_VERSION:=293b73818e113bf4544bc1aa636495f1b2f0832d
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION)-$(PKG_SOURCE_VERSION).tar.gz

include $(INCLUDE_DIR)/package.mk

define Package/bossa
  SECTION:=utils
  CATEGORY:=Utilities
  DEPENDS:=+libstdcpp
  TITLE:=Utility to flash ARM microcontrollers
endef

define Package/bossa/description
 BOSSA is a flash programming utility for Atmel's SAM family of flash-based
 ARM microcontrollers. The motivation behind BOSSA is to create a simple,
 easy-to-use, open source utility to replace Atmel's SAM-BA software.
endef

define Build/Compile
	$(MAKE) -C $(PKG_BUILD_DIR) $(TARGET_CONFIGURE_OPTS) CFLAGS="$(TARGET_CFLAGS)" bin/bossac
endef

define Package/bossa/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/bin/bossac $(1)/usr/bin/
endef

$(eval $(call BuildPackage,bossa))
