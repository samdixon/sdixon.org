const { cwd, stdout, copy } = Deno;
import { serve } from "https://deno.land/x/sift@0.5.0/mod.ts";
import { renderFile } from 'https://deno.land/x/dejs/mod.ts';

const templateDir = "templates";

async function renderTemplateSync(path) {
  return new Response(await renderFile(`${templateDir}/${path}`), {
    headers: {
      'content-type': 'text/html'
    }
  })
}

serve({
  "/": () => renderTemplateSync('index.ejs'),
  "/projects": () => renderTemplateSync('projects.ejs'),
  "/about": () => renderTemplateSync('about.ejs'),
  "/blog": () => renderTemplateSync('blog.ejs'),
  "/blog/:slug": (_req, _conn, params) => {
    const post = `Hello, you visited ${params.slug}!`;
    return new Response(post);
  },
  // The route handler of 404 will be invoked when a route handler
  // for the requested path is not found.
  404: () => new Response("not found"),
});