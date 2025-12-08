//src/api/index.js 

/* Auto-import all *Api.js modules in this directory. Works with both default and named exports */
const modules = import.meta.glob('./*Api.js', { eager: true });

/* Consolidate all API exports into a single object */
const api = {};

for (const path in modules) {

    const mod = modules[path];

    /* Extract file name */
    const fileName = path.split('/').pop();

    if (!fileName.endsWith('Api.js')) continue;

    /* Normalized module name base */
    const moduleName = fileName.replace('.js', '');

    /* Handle default and named exports */
    if (mod.default) {
        api[moduleName] = mod.default;
    } else {
        api[moduleName] = mod;
    }   
}

export default api;
export const { authApi } = api;
