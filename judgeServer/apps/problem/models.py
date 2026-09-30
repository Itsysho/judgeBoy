# CREATE TABLE `problems` (
#   `pid` int(11) NOT NULL AUTO_INCREMENT,
#   `pub` int(11) NOT NULL, // is public
#   `ts` bigint(20) DEFAULT NULL, // timestamp
#   `src` text COLLATE utf8_unicode_ci NOT NULL, // source
#   `ttl` text COLLATE utf8_unicode_ci NOT NULL, // title
#   `level` int(11) DEFAULT NULL, // difficulty level
#   `porder` int(11) DEFAULT NULL, // pre order
#   PRIMARY KEY (`pid`)
# ) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

from django.db import models


class Problem(models.Model):
    public_status = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(null=True, blank=True)
    src = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    level = models.IntegerField(null=True, blank=True)
    post_order = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["post_order", "id"]
