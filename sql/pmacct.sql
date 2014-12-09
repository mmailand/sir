CREATE TABLE "acct" (
        `mac_src`       CHAR(17) NOT NULL DEFAULT '0:0:0:0:0:0',
        `mac_dst`       CHAR(17) NOT NULL DEFAULT '0:0:0:0:0:0',
        `ip_src`        CHAR(15) NOT NULL DEFAULT '0.0.0.0',
        `ip_dst`        CHAR(15) NOT NULL DEFAULT '0.0.0.0',
        `mask_dst`      INTEGER(1),
        `src_port`      INT(4) NOT NULL DEFAULT 0,
        `dst_port`      INT(4) NOT NULL DEFAULT 0,
        `ip_proto`      CHAR(6) NOT NULL DEFAULT 0,
        `packets`       INT NOT NULL,
        `bytes` BIGINT NOT NULL,
        `stamp_inserted`        DATETIME NOT NULL DEFAULT '0000-00-00 00:00:00',
        `stamp_updated` DATETIME,
        PRIMARY KEY(mac_src,mac_dst,ip_src,ip_dst,src_port,dst_port,ip_proto,stamp_inserted)
);
