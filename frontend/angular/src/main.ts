import { bootstrapApplication } from "@angular/platform-browser";
import { Component } from "@angular/core";

@Component({
  selector: "app-root",
  standalone: true,
  template: `<main class="shell"><h1>Angular listo en Docker</h1><p>Campuslands Docker Stack</p></main>`,
  styles: [`body{margin:0}.shell{min-height:100vh;display:grid;place-content:center;text-align:center;font-family:Arial;background:#3b0764;color:white}h1{color:#f0abfc}`]
})
class AppComponent {}

bootstrapApplication(AppComponent);
