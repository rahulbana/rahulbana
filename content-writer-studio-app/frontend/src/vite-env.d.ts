// ---------------------------------------------------------------------------
// Name:     Rahul Singh Bana
// Email:    bana.saa@gmail.com
// LinkedIn: https://www.linkedin.com/in/rahulsinghbana
// Repo:     https://github.com/rahulbana/rahulbana
// ---------------------------------------------------------------------------
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL?: string;
  readonly VITE_API_PROXY?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
