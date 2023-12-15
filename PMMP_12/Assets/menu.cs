using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class menu : MonoBehaviour
{
    public void LoadScene(string sceneName)
    {
        SceneManager.LoadScene(sceneName);
    }

    public void ButtonClick()
    {
        LoadScene("1");
    }

    public void Button1Click()
    {
        LoadScene("3");
    }

}
