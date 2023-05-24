import Cookies from 'js-cookie'

const TokenKey = 'token'

export function getTokenCookie() {
  return Cookies
}

export function setTokenCookie(token) {
  return Cookies.set(TokenKey, token, { expires: 7 })
}

export function removeTokenCookie() {
  return Cookies.remove(TokenKey)
}