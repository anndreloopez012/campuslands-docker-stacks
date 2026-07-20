using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);
var connection = builder.Configuration.GetConnectionString("Default");
builder.Services.AddDbContext<AppDbContext>(options => options.UseNpgsql(connection));
var app = builder.Build();

app.MapGet("/", async (AppDbContext db) =>
{
    var canConnect = await db.Database.CanConnectAsync();
    return Results.Json(new { stack = ".NET Entity Framework + PostgreSQL", database = canConnect ? "ok" : "sin conexion" });
});

app.Run();

class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options) { }
