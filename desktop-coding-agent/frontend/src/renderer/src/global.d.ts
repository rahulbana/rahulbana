// ---------------------------------------------------------------------------
// Name:     Rahul Singh Bana
// Email:    bana.saa@gmail.com
// LinkedIn: https://www.linkedin.com/in/rahulsinghbana
// Repo:     https://github.com/rahulbana/rahulbana
// ---------------------------------------------------------------------------
import type { DesktopBridge } from '../../shared/types'

declare global {
  interface Window {
    desktop: DesktopBridge
  }
}

export {}
