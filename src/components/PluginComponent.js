import React, { Component } from 'react'
import {AwesomeComponent} from 'da-host'
class PluginComponent extends Component {
  render () {
    return (
      <div style={{border: '1px solid black'}}>
        This is Plugin Component
        <AwesomeComponent/>
      </div>
    )
  }
}

export default PluginComponent
