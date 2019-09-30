database (MySQL):

CREATE TABLE  `lecker`.`bookmarks` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `url` text NOT NULL,
  `created` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `tags` text NOT NULL,
  `title` text NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `id` (`id`)
);
