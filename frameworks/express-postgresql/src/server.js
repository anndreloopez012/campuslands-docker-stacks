const express = require("express");
const { Pool } = require("pg");
const app = express();
const pool = new Pool({ host: "postgres", database: process.env.POSTGRES_DB, user: process.env.POSTGRES_USER, password: process.env.POSTGRES_PASSWORD });
app.get("/", async (_req, res) => { const db = await pool.query("select now() as now"); res.json({ stack: "Express + PostgreSQL", dbTime: db.rows[0].now }); });
app.listen(3330, () => console.log("Express listo en puerto 3330"));
