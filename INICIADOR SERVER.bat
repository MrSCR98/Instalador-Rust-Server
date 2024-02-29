@echo off
RustDedicated.exe -batchmode -nographics ^
+server.hostname "Nombre de servidor" ^
+server.description "Instalador-Rust-Server" ^
+server.headerimage "" ^
+server.url "" ^
+server.ip 0.0.0.0 ^
+server.port 28015 ^
+server.maxplayers 100 ^
+rcon.ip 0.0.0.0 ^
+rcon.port 28016 ^
+rcon.password "cambia#estañc0ntraseña" ^
+server.identity "default" ^
+server.level "Procedural Map" ^
+server.seed 5658512 +server.worldsize 4000 ^
+server.radiation "True" ^
+bradley.enabled "True" ^
+bradley.respawndelayminutes "60" ^
+bradley.respawndelayvariance "1" ^
+heli.lifetimeminutes "15" ^
+server.stability "True" ^
+decay.upkeep "True" ^
+decay.upkeep_heal_scale "1" ^
+decay.upkeep_inside_decay_scale "0.1" ^
+decay.upkeep_period_minutes "1440" ^
+rcon.web "True" ^
-logfile "logfilename.log" ^

